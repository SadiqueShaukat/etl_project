import yaml
import logging
import logging.handlers
import os

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Failed to load config: {e}")
        raise

def setup_logging(log_path, log_level):
    logger = logging.getLogger('ETL')
    logger.setLevel(getattr(logging, log_level))
    handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=1048576, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger