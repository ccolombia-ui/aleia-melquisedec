"""
PyKEEN Training Script for Library Ontology Embeddings
Purpose: Train TransE model on biblioteca triples for semantic similarity
Requirements: Python 3.11+, pykeen, torch
"""

import sys
from pathlib import Path
import yaml
import torch
from pykeen.pipeline import pipeline
from pykeen.triples import TriplesFactory
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
CONFIG_FILE = Path("pykeen_config.yaml")
OUTPUT_DIR = Path("results")
ONTOLOGY_FILE = Path("../../hito-2-conceptualizacion/templates-ottr-automatizacion/output/library-ontology-example.ttl")

def convert_ttl_to_tsv(ttl_file: Path, output_tsv: Path):
    """Convert TTL triples to TSV format for PyKEEN"""
    from rdflib import Graph
    
    logger.info(f"Loading ontology: {ttl_file}")
    g = Graph()
    g.parse(str(ttl_file), format="turtle")
    
    logger.info(f"Converting {len(g)} triples to TSV format")
    
    with open(output_tsv, 'w', encoding='utf-8') as f:
        for subj, pred, obj in g:
            # Only include triples with named resources (skip literals for link prediction)
            if str(obj).startswith('http://'):
                f.write(f"{subj}\t{pred}\t{obj}\n")
    
    logger.info(f"Wrote {output_tsv}")

def split_triples(all_triples_file: Path, train_ratio=0.8, valid_ratio=0.1):
    """Split triples into train/valid/test sets"""
    import pandas as pd
    from sklearn.model_selection import train_test_split
    
    # Read all triples
    df = pd.read_csv(all_triples_file, sep='\t', header=None, names=['head', 'relation', 'tail'])
    
    logger.info(f"Total triples: {len(df)}")
    
    # First split: separate test set
    train_valid, test = train_test_split(df, test_size=(1 - train_ratio - valid_ratio), random_state=42)
    
    # Second split: separate validation from training
    train, valid = train_test_split(train_valid, test_size=(valid_ratio / (train_ratio + valid_ratio)), random_state=42)
    
    # Save splits
    train.to_csv('training_triples.tsv', sep='\t', header=False, index=False)
    valid.to_csv('validation_triples.tsv', sep='\t', header=False, index=False)
    test.to_csv('testing_triples.tsv', sep='\t', header=False, index=False)
    
    logger.info(f"Train: {len(train)}, Valid: {len(valid)}, Test: {len(test)}")

def load_config(config_file: Path) -> dict:
    """Load PyKEEN configuration from YAML"""
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def train_model(config: dict):
    """Train PyKEEN model using pipeline"""
    logger.info("Starting PyKEEN training pipeline")
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Run pipeline
    result = pipeline(
        training='training_triples.tsv',
        testing='testing_triples.tsv',
        validation='validation_triples.tsv',
        model=config['pipeline']['model'],
        model_kwargs=config['pipeline']['model_kwargs'],
        training_loop=config['pipeline']['training_loop'],
        training_kwargs=config['pipeline']['training_kwargs'],
        optimizer=config['pipeline']['optimizer'],
        optimizer_kwargs=config['pipeline']['optimizer_kwargs'],
        loss=config['pipeline']['loss'],
        loss_kwargs=config['pipeline']['loss_kwargs'],
        evaluator=config['pipeline']['evaluator'],
        evaluator_kwargs=config['pipeline']['evaluator_kwargs'],
        negative_sampler=config['pipeline']['negative_sampler'],
        negative_sampler_kwargs=config['pipeline']['negative_sampler_kwargs'],
        stopper=config['pipeline']['stopper'],
        stopper_kwargs=config['pipeline']['stopper_kwargs'],
        random_seed=config['random_seed'],
        device=config['device']
    )
    
    logger.info("Training complete!")
    
    # Save model
    model_path = OUTPUT_DIR / "model.pkl"
    result.save_to_directory(str(OUTPUT_DIR))
    logger.info(f"Model saved to {OUTPUT_DIR}")
    
    # Save entity and relation embeddings
    entity_embeddings = result.model.entity_representations[0](indices=None).detach().cpu().numpy()
    relation_embeddings = result.model.relation_representations[0](indices=None).detach().cpu().numpy()
    
    import pandas as pd
    
    # Entity embeddings to TSV
    entity_to_id = result.training.entity_to_id
    entities_df = pd.DataFrame(entity_embeddings, index=list(entity_to_id.keys()))
    entities_df.to_csv(OUTPUT_DIR / "entity_embeddings.tsv", sep='\t')
    
    # Relation embeddings to TSV
    relation_to_id = result.training.relation_to_id
    relations_df = pd.DataFrame(relation_embeddings, index=list(relation_to_id.keys()))
    relations_df.to_csv(OUTPUT_DIR / "relation_embeddings.tsv", sep='\t')
    
    logger.info(f"Embeddings saved: {OUTPUT_DIR / 'entity_embeddings.tsv'}")
    
    # Print metrics
    logger.info("\n" + "="*50)
    logger.info("Evaluation Metrics:")
    logger.info("="*50)
    for metric, value in result.metric_results.to_dict().items():
        logger.info(f"{metric}: {value:.4f}")
    
    return result

def main():
    logger.info("="*50)
    logger.info("PyKEEN Training Pipeline")
    logger.info("="*50)
    
    # Check if ontology file exists
    if not ONTOLOGY_FILE.exists():
        logger.error(f"Ontology file not found: {ONTOLOGY_FILE}")
        logger.info("Please generate TTL output using Lutra first:")
        logger.info("  cd ../../hito-2-conceptualizacion/templates-ottr-automatizacion/")
        logger.info("  lutra --library ottr-templates/ --input instances/*.ottrinst --output output/library-ontology.ttl")
        return 1
    
    # Step 1: Convert TTL to TSV
    if not Path('all_triples.tsv').exists():
        logger.info("Step 1: Converting TTL to TSV")
        convert_ttl_to_tsv(ONTOLOGY_FILE, Path('all_triples.tsv'))
    else:
        logger.info("Step 1: Skipped (all_triples.tsv already exists)")
    
    # Step 2: Split triples
    if not all([Path(f).exists() for f in ['training_triples.tsv', 'validation_triples.tsv', 'testing_triples.tsv']]):
        logger.info("Step 2: Splitting triples into train/valid/test")
        split_triples(Path('all_triples.tsv'))
    else:
        logger.info("Step 2: Skipped (split files already exist)")
    
    # Step 3: Load config
    if not CONFIG_FILE.exists():
        logger.error(f"Config file not found: {CONFIG_FILE}")
        return 1
    
    logger.info(f"Step 3: Loading config from {CONFIG_FILE}")
    config = load_config(CONFIG_FILE)
    
    # Step 4: Train model
    logger.info("Step 4: Training TransE model")
    result = train_model(config)
    
    logger.info("\n" + "="*50)
    logger.info("Training Complete!")
    logger.info("="*50)
    logger.info(f"Model saved to: {OUTPUT_DIR}")
    logger.info(f"Embeddings: {OUTPUT_DIR / 'entity_embeddings.tsv'}")
    logger.info(f"Evaluation: {OUTPUT_DIR / 'evaluation.json'}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
