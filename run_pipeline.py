
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import logging

logger = logging.getLogger('ETL')

def run_pipeline(config):
    try:
        data = extract_data(config['input_path'])
        transformed_data = transform_data(data)
        load_data(transformed_data, config['output_db'])
        logger.info("ETL pipeline completed successfully")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise
