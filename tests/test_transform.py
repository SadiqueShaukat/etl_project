import pytest
import pandas as pd
from src.transform import transform_data

def test_transform_data():
    data = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', None],
        'age': [25, None],
        'salary': [50000, 60000]
    })
    transformed = transform_data(data)
    assert transformed['name'][1] == 'Unknown'
    assert transformed['age'][1] == 25
    assert 'salary_in_k' in transformed.columns