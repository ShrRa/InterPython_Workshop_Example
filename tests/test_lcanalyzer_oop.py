"""Tests for Survey class within the Model layer."""

import pandas as pd
import pytest
import numpy as np

# Parametrization for  function testing
@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        pytest.approx(3.66,0.01)),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_mean_mag(test_df, test_colname, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from lcanalyzer.models import mean_mag
    assert mean_mag(test_df, test_colname) == expected