"""
Evaluation Metrics Script for PyKEEN Embeddings
Purpose: Evaluate trained model and generate visualizations
Requirements: Python 3.11+, pykeen, matplotlib, sklearn
"""

import sys
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
RESULTS_DIR = Path("results")
EMBEDDINGS_FILE = RESULTS_DIR / "entity_embeddings.tsv"
OUTPUT_DIR = Path("evaluation_output")

def load_embeddings(embeddings_file: Path):
    """Load entity embeddings from TSV"""
    logger.info(f"Loading embeddings from {embeddings_file}")
    df = pd.read_csv(embeddings_file, sep='\t', index_col=0)
    logger.info(f"Loaded {len(df)} entity embeddings of dimension {df.shape[1]}")
    return df

def generate_tsne_plot(embeddings_df: pd.DataFrame, output_file: Path):
    """Generate t-SNE 2D visualization of embeddings"""
    logger.info("Generating t-SNE visualization (this may take a minute)...")
    
    # Run t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(embeddings_df)-1))
    embeddings_2d = tsne.fit_transform(embeddings_df.values)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Color code by entity type (based on URI patterns)
    colors = []
    labels_text = []
    for entity in embeddings_df.index:
        entity_str = str(entity)
        if 'Libro' in entity_str or 'Book' in entity_str:
            colors.append('blue')
        elif 'Autor' in entity_str or 'Author' in entity_str:
            colors.append('red')
        elif 'Categoria' in entity_str or 'Category' in entity_str:
            colors.append('green')
        elif 'Usuario' in entity_str or 'User' in entity_str:
            colors.append('orange')
        elif 'Prestamo' in entity_str or 'Loan' in entity_str:
            colors.append('purple')
        else:
            colors.append('gray')
        
        # Extract entity name for label
        if '#' in entity_str:
            labels_text.append(entity_str.split('#')[-1])
        elif '/' in entity_str:
            labels_text.append(entity_str.split('/')[-1])
        else:
            labels_text.append(entity_str[:20])
    
    # Scatter plot
    scatter = ax.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c=colors, alpha=0.6, s=100)
    
    # Add labels for top entities
    for i, txt in enumerate(labels_text[:20]):  # Only label first 20 for readability
        ax.annotate(txt, (embeddings_2d[i, 0], embeddings_2d[i, 1]), fontsize=8, alpha=0.7)
    
    ax.set_title('t-SNE Visualization of Entity Embeddings', fontsize=14, fontweight='bold')
    ax.set_xlabel('t-SNE Dimension 1')
    ax.set_ylabel('t-SNE Dimension 2')
    ax.grid(True, alpha=0.3)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='blue', label='Libro/Book'),
        Patch(facecolor='red', label='Autor/Author'),
        Patch(facecolor='green', label='Categoria'),
        Patch(facecolor='orange', label='Usuario/User'),
        Patch(facecolor='purple', label='Prestamo/Loan'),
        Patch(facecolor='gray', label='Other')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"t-SNE plot saved to {output_file}")
    plt.close()

def compute_similarity_matrix(embeddings_df: pd.DataFrame, top_n=10):
    """Compute cosine similarity between entities"""
    from sklearn.metrics.pairwise import cosine_similarity
    
    logger.info("Computing cosine similarity matrix...")
    
    # Compute similarities
    similarity_matrix = cosine_similarity(embeddings_df.values)
    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=embeddings_df.index,
        columns=embeddings_df.index
    )
    
    # Find top N similar pairs
    logger.info(f"\nTop {top_n} Most Similar Entity Pairs:")
    logger.info("="*60)
    
    # Get upper triangle indices (avoid duplicates and self-similarity)
    upper_tri_indices = np.triu_indices(len(similarity_df), k=1)
    similarities = []
    
    for i, j in zip(upper_tri_indices[0], upper_tri_indices[1]):
        entity1 = similarity_df.index[i]
        entity2 = similarity_df.index[j]
        sim = similarity_df.iloc[i, j]
        similarities.append((entity1, entity2, sim))
    
    # Sort by similarity
    similarities.sort(key=lambda x: x[2], reverse=True)
    
    results = []
    for rank, (e1, e2, sim) in enumerate(similarities[:top_n], 1):
        # Extract entity names
        e1_name = str(e1).split('#')[-1].split('/')[-1]
        e2_name = str(e2).split('#')[-1].split('/')[-1]
        logger.info(f"{rank}. {e1_name} <-> {e2_name}: {sim:.4f}")
        results.append({
            "rank": rank,
            "entity1": e1_name,
            "entity2": e2_name,
            "similarity": float(sim)
        })
    
    return results

def load_evaluation_metrics():
    """Load evaluation metrics from PyKEEN results"""
    metrics_file = RESULTS_DIR / "results.json"
    
    if not metrics_file.exists():
        logger.warning(f"Metrics file not found: {metrics_file}")
        return None
    
    with open(metrics_file, 'r') as f:
        results = json.load(f)
    
    # Extract metrics
    metrics = results.get('metrics', {})
    
    logger.info("\n" + "="*60)
    logger.info("Evaluation Metrics Summary:")
    logger.info("="*60)
    
    for metric, value in metrics.items():
        if 'realistic' in metric.lower() or 'both' in metric.lower():
            logger.info(f"{metric}: {value:.4f}")
    
    return metrics

def generate_metrics_report(metrics: dict, similarity_results: list, output_file: Path):
    """Generate comprehensive metrics report"""
    report = {
        "evaluation_metrics": metrics if metrics else {},
        "top_similar_pairs": similarity_results,
        "interpretation": {
            "hits_at_10": "Percentage of correct entities in top 10 predictions",
            "mean_rank": "Average position of correct entity in ranked list (lower is better)",
            "mean_reciprocal_rank": "Average of 1/rank (higher is better, range 0-1)"
        },
        "recommendations": []
    }
    
    # Add recommendations based on metrics
    if metrics:
        hits_10 = metrics.get('hits_at_10.realistic.both.avg', 0)
        mean_rank = metrics.get('mean_rank.realistic.both.avg', float('inf'))
        
        if hits_10 < 0.5:
            report["recommendations"].append({
                "metric": "hits_at_10",
                "issue": f"Low Hits@10 ({hits_10:.2f})",
                "suggestion": "Increase training epochs (500→1000) or try different model (DistMult, ComplEx)"
            })
        
        if mean_rank > 100:
            report["recommendations"].append({
                "metric": "mean_rank",
                "issue": f"High Mean Rank ({mean_rank:.0f})",
                "suggestion": "Add more training triples or increase embedding dimension (100→200)"
            })
    
    # Save report
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    logger.info(f"\nComprehensive report saved to {output_file}")

def main():
    logger.info("="*60)
    logger.info("PyKEEN Evaluation & Visualization")
    logger.info("="*60)
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Check if embeddings exist
    if not EMBEDDINGS_FILE.exists():
        logger.error(f"Embeddings file not found: {EMBEDDINGS_FILE}")
        logger.info("Please run train_embeddings.py first")
        return 1
    
    # Step 1: Load embeddings
    embeddings_df = load_embeddings(EMBEDDINGS_FILE)
    
    # Step 2: Generate t-SNE visualization
    tsne_plot_file = OUTPUT_DIR / "tsne_visualization.png"
    generate_tsne_plot(embeddings_df, tsne_plot_file)
    
    # Step 3: Compute similarity matrix
    similarity_results = compute_similarity_matrix(embeddings_df, top_n=15)
    
    # Step 4: Load evaluation metrics
    metrics = load_evaluation_metrics()
    
    # Step 5: Generate comprehensive report
    report_file = OUTPUT_DIR / "evaluation_report.json"
    generate_metrics_report(metrics, similarity_results, report_file)
    
    logger.info("\n" + "="*60)
    logger.info("Evaluation Complete!")
    logger.info("="*60)
    logger.info(f"Outputs:")
    logger.info(f"  - t-SNE plot: {tsne_plot_file}")
    logger.info(f"  - Report: {report_file}")
    logger.info(f"  - Embeddings: {EMBEDDINGS_FILE}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
