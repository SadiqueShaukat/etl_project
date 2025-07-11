import pytest
import pandas as pd
import sqlite3
from src.load import load_data

def test_load_data(tmp_path):
    db_path = tmp_path / "test.db"
    data = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob'],
        'age': [25, 30],
        'salary': [50000, 60000]
    })
    load_data(data, str(db_path))
    conn = sqlite3.connect(str(db_path))
    result = pd.read_sql("SELECT * FROM employees", conn)
    conn.close()
    assert len(result) == 2
    assert list(result.columns) == ['id', 'name', 'age', 'salary']