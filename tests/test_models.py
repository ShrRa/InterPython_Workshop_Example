"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected


# Parametrization for mean_mag function testing 
# with approximate comparison
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
    

def test_min_mag_negatives():
    # Test that min_mag function works for negatives
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[-7, -7, -3], [-4, -3, -1], [-1, -5, -3]], columns=list("abc"))
    test_input_colname = "b"
    test_output = -7

    assert min_mag(test_input_df, test_input_colname) == test_output


def test_mean_mag_integers():
    # Test that mean_mag function works for integers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[-7, 8, -3], [0, -3, -1], [10, -5, 5]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 1.

    assert mean_mag(test_input_df, test_input_colname) == test_output


def test_calc_stat_integers():
    # Test that calc_stat function works for integers
    from lcanalyzer.models import calc_stat

    df1 = pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc"))
    df2 = pd.DataFrame(data=[[7, 3, 2], [8, 4, 2], [5, 6, 4]], columns=list("abc"))
    df3 = pd.DataFrame(data=[[2, 6, 3], [1, 3, 6], [8, 9, 1]], columns=list("abc"))
    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = {"df1_max": 8, "df2_max": 6, "df3_max": 9}
    test_output == calc_stat(test_input, ["df1", "df2", "df3"], "b")

    assert calc_stat(test_input, ["df1", "df2", "df3"], "b") == test_output

def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)

# Old versions of tests
"""
def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output
"""
