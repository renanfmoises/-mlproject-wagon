import mlproject
import pandas as pd
# Import from our lib
from mlproject.distance import haversine
import pytest

def test_distance():
    out = haversine(48.865070, 2.380009, 48.235070, 2.393409)
    assert type(out) == float
    assert out == 70.00789153218594
    print('All tests passed!')
