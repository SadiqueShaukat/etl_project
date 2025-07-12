import pandas as pd
import logging

logger = logging.getLogger('ETL')

def extract_data(file_path):
    try:
        logger.info(f"Extracting data from {file_path}")
        data = pd.read_csv(file_path)
        logger.info(f"Extracted {len(data)} records")
        return data
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
