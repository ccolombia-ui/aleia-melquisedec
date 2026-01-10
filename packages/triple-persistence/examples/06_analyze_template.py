#!/usr/bin/env python3
"""
Analyze an entire template folder for semantic gaps, coherence, and duplication.

This script attempts to run the full ingestion + retrieval pipeline (requires
Neo4j and Ollama). If the live services are not available it falls back to an
"offline" text-based analysis (simple token overlap / cosine on bag-of-words)
so you can still get useful gap/duplication/coherence reports locally.

Target folder: apps/research-autopoietic-template
"""

import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

# Ensure package import
sys.path.insert(0, str(Path(__file__).parent.parent))

from triple_persistence.ingestion import TriplePersistencePipeline
from triple_persistence.models import IngestionConfig, QueryRequest
from triple_persistence.retriever import HybridRetriever


def tokenize(text: str) -> List[str]:
    text = text.lower()
    tokens = re.findall(r"\b[a-z]{3,}\b", text)
    return tokens


def cosine_sim(a: Dict[str, int], b: Dict[str, int]) -> float:
    # simple bag-of-words cosine similarity
    common = set(a.keys()) & set(b.keys())
    num = sum(a[k] * b[k] for k in common)
    sum_a = sum(v * v for v in a.values())
    sum_b = sum(v * v for v in b.values())
    denom = math.sqrt(sum_a) * math.sqrt(sum_b)
    if denom == 0:
        return 0.0
    return num / denom


def load_markdown_texts(folder: Path) -> Dict[str, str]:
    docs = {}
    for p in folder.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:
            txt = p.read_text(encoding="latin-1")
        docs[str(p)] = txt
    return docs


def build_bow(text: str) -> Dict[str, int]:
    tokens = tokenize(text)
    return Counter(tokens)


def detect_duplicates(
    docs: Dict[str, str], threshold: float = 0.85
) -> List[Tuple[str, str, float]]:
    paths = list(docs.keys())
    bows = {p: build_bow(docs[p]) for p in paths}
    duplicates = []
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            a = bows[paths[i]]
            b = bows[paths[j]]
            s = cosine_sim(a, b)
            if s >= threshold:
                duplicates.append((paths[i], paths[j], s))
    return duplicates


def extract_headings(text: str) -> List[str]:
    return re.findall(r"^##+\s*(.+)$", text, flags=re.MULTILINE)


def semantic_gap_analysis(manifesto_text: str, docs: Dict[str, str]) -> List[Tuple[str, float]]:
    headings = extract_headings(manifesto_text)
    gaps = []
    for h in headings:
        # simple keyword coverage: count docs that mention 2+ words from heading
        keywords = [w for w in re.findall(r"\b\w{4,}\b", h.lower())]
        if not keywords:
            continue
        count_cover = 0
        for txt in docs.values():
            txt_lower = txt.lower()
            match_words = sum(1 for kw in keywords if kw in txt_lower)
            if match_words >= max(1, len(keywords) // 3):
                count_cover += 1
        coverage = count_cover / max(1, len(docs))
        if coverage < 0.2:
            gaps.append((h, coverage))
    return gaps


def coherence_score(text: str) -> float:
    # Split into paragraphs and compute average pairwise similarity
    paras = [p for p in re.split(r"\n\n+", text) if len(p.strip()) > 50]
    if len(paras) < 2:
        return 1.0
    bows = [build_bow(p) for p in paras]
    sims = []
    for i in range(len(bows)):
        for j in range(i + 1, len(bows)):
            sims.append(cosine_sim(bows[i], bows[j]))
    return sum(sims) / max(1, len(sims))


def generate_report(template_folder: Path) -> Dict[str, any]:
    print("\nStarting offline analysis of folder:", template_folder)
    docs = load_markdown_texts(template_folder)
    manifest_path = template_folder / "010-define" / "inputs" / "raw-manifiesto.md"
    manifesto_text = docs.get(str(manifest_path), "")

    report = {
        "total_documents": len(docs),
        "duplicates": [],
        "semantic_gaps": [],
        "coherence": {},
    }

    if len(docs) == 0:
        return report

    # Duplicates
    duplicates = detect_duplicates(docs, threshold=0.85)
    report["duplicates"] = duplicates

    # Semantic gaps using manifesto headings as expectations
    if manifesto_text:
        gaps = semantic_gap_analysis(manifesto_text, docs)
        report["semantic_gaps"] = gaps

    # Coherence per document
    for path, txt in docs.items():
        score = coherence_score(txt)
        report["coherence"][path] = score

    return report


def main():
    base = Path("C:/proyectos/aleia-melquisedec/apps/research-autopoietic-template")
    if not base.exists():
        print("Folder not found:", base)
        return 1

    # Try full pipeline ingestion if services available
    try:
        config = IngestionConfig(
            project="research-autopoietic-template",
            paths=[str(base)],
            neo4j_uri="bolt://localhost:7687",
            neo4j_user="neo4j",
            neo4j_password="password",
            ollama_base_url="http://localhost:11434",
            embedding_model="nomic-embed-text",
        )

        print("Attempting live ingestion with TriplePersistencePipeline (requires Neo4j/Ollama)...")
        with TriplePersistencePipeline(config) as pipeline:
            pipeline.ingest_directory(str(base))
            retriever = HybridRetriever(
                index=pipeline.index, neo4j_driver=pipeline.neo4j_driver, project=config.project
            )

            # Example query to check health
            req = QueryRequest(
                query="¿Qué son templates autopoiéticos?", top_k=5, include_graph=True
            )
            resp = retriever.query(req)
            print("Live retrieval sample results:", resp.total_results)

            # If we are here, run knowledge-base stats
            stats = retriever.get_stats()
            print("KB stats:", stats)

            # We will also export an offline report as fallback
    except Exception as e:
        print("Live ingestion not possible (services missing or error):", e)
        print("Proceeding with offline text-based analysis...")

    report = generate_report(base)

    # Present a concise report
    print("\n=== Analysis Report Summary ===")
    print(f"Total documents: {report['total_documents']}")
    print(f"Duplicates found: {len(report['duplicates'])}")
    if report["duplicates"]:
        for a, b, s in report["duplicates"]:
            print(f" - DUP: {Path(a).name} <-> {Path(b).name} (sim={s:.2f})")

    print(f"Semantic gaps detected: {len(report.get('semantic_gaps', []))}")
    if report.get("semantic_gaps"):
        for h, cov in report["semantic_gaps"]:
            print(f" - GAP: '{h[:80]}...' coverage={cov:.2f}")

    print("\nCoherence (document -> score 0..1):")
    low = [(p, s) for p, s in report["coherence"].items() if s < 0.3]
    print(f"  Documents with low coherence (<0.3): {len(low)}")
    for p, s in low:
        print(f"   - {Path(p).name}: {s:.2f}")

    # Recommendations (minimalist)
    print("\nRecommended next steps:")
    print(" 1. Merge or remove identified duplicates; pick one canonical file per topic.")
    print(
        " 2. Create a minimal TOC driven by manifesto headings and assign single source of truth per heading."
    )
    print(" 3. Add cross-ref fields (e.g., 'canonical_for: <heading>') and enforce via CI checks.")
    print(" 4. Tag documents with a small controlled vocabulary (10-20 tags) and assign rostros.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
