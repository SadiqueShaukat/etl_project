import pytest
import pandas as pd
from src.extract import extract_data

def test_extract_data():
    df = extract_data('data/input/sample_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert list(df.columns) == ['id', 'name', 'age', 'salary']