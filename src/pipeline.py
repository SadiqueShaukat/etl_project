import sqlite3
from src.config import load_config, setup_logging
from src.pipeline import run_pipeline

if __name__ == "__main__":
    config = load_config('config/config.yaml')
    logger = setup_logging(config['log_path'], config['log_level'])
    conn = sqlite3.connect(config['output_db'])
    with open('data/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.close()
    run_pipeline(config)