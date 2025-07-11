import sqlite3
import pandas as pd
import logging

logger = logging.getLogger('ETL')

def load_data(data, db_path, table_name='employees'):
    try:
        logger.info(f"Loading data to {db_path}")
        conn = sqlite3.connect(db_path)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        logger.info(f"Loaded {len(data)} records to {table_name}")
    except Exception as e:
        logger.error(f"Load failed: {e}")
        raise