import pandas as pd
import logging

logger = logging.getLogger('ETL')

def transform_data(data):
    try:
        logger.info("Starting data transformation")
        data['name'] = data['name'].fillna('Unknown')
        data['age'] = data['age'].fillna(data['age'].median())
        data['salary_in_k'] = data['salary'] / 1000
        logger.info("Transformation completed")
        return data
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        raise