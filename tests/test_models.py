"""Tests for statistics functions within the Model layer."""

import pandas as pd
import numpy as np
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
        (pd.DataFrame(data=[[1, 5, 3],
                            [7, 8, 9],
                            [np.nan, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected


def test_max_mag_strings():
    '''Test for TypeError when passing a string'''
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)


@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        1),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
        (pd.DataFrame(data=[[1, 5, 3],
                            [7, 8, 9],
                            [np.nan, 4, 1]], 
                      columns=list("abc")),
        "a",
        1),
    ])
def test_min_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import min_mag
    assert min_mag(test_df, test_colname) == expected

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        11/3.),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
        (pd.DataFrame(data=[[1, 5, 3],
                            [7, 8, 9],
                            [np.nan, 4, 1]], 
                      columns=list("abc")),
        "a",
        4),
    ])
def test_mean_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import mean_mag
    assert mean_mag(test_df, test_colname) == expected

@pytest.mark.parametrize(
    "test_df, bands, test_colname, stat, expected",
    [
        ({"df1": pd.DataFrame(data=[[1, 5, 3],
                                     [7, 8, 9],
                                     [3, 4, 1]], columns=list("abc")),
          "df2": pd.DataFrame(data=[[7, 3, 2],
                                    [8, 4, 2],
                                    [5, 6, 4]], columns=list("abc")),
          "df3": pd.DataFrame(data=[[2, 6, 3],
                                    [1, 3, 6],
                                    [8, 9, 1]], columns=list("abc"))},
        ["df1", "df2", "df3"],
        "b",
        "max",
        {"df1_max": 8, "df2_max": 6, "df3_max": 9}),
        ({"df1": pd.DataFrame(data=[[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]], columns=list("abc")),
          "df2": pd.DataFrame(data=[[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]], columns=list("abc")),
          "df3": pd.DataFrame(data=[[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]], columns=list("abc"))},
        ["df1", "df2", "df3"],
        "b",
        "max",
        {"df1_max": 0, "df2_max": 0, "df3_max": 0}),
        ({"df1": pd.DataFrame(data=[[1, np.nan, 3],
                                    [7, 8, 9],
                                    [3, 4, 1]], columns=list("abc")),
          "df2": pd.DataFrame(data=[[7, 3, 2],
                                    [8, np.nan, 2],
                                    [5, 6, 4]], columns=list("abc")),
          "df3": pd.DataFrame(data=[[2, 6, 3],
                                    [1, np.nan, 6],
                                    [8, 9, 1]], columns=list("abc"))},
        ["df1", "df2", "df3"],
        "b",
        "max",
        {"df1_max": 8, "df2_max": 6, "df3_max": 9}),
        ({"df1": pd.DataFrame(data=[[1, 5, 3],
                                    [7, 8, 9],
                                    [3, 4, 1]], columns=list("abc")),
          "df2": pd.DataFrame(data=[[7, 3, 2],
                                    
                                    [8, 4, 2],
                                    [5, 6, 4]], columns=list("abc")),
          "df3": pd.DataFrame(data=[[2, 6, 3],
                                    [1, 3, 6],
                                    [8, 9, 1]], columns=list("abc"))},
        ["df1", "df2", "df3"],
        "b",
        "mean",
        {"df1_mean": 17/3., "df2_mean": 13/3., "df3_mean": 6}),
    ])
def test_calc_stat(test_df, bands, test_colname, stat, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import calc_stat
    assert calc_stat(test_df, bands, test_colname, stat) == expected
    
# Parametrization for normalize_lc function testing with ValueError
@pytest.mark.parametrize(
    "test_input_df, test_input_colname, expected, expected_raises",
    [
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, 4, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285]),
        None),
        (pd.DataFrame(data=[[1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.]),
        None),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.]),
        None),
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, -99.9, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285]),
        ValueError),
    ])
def test_normalize_lc(test_input_df, test_input_colname, expected,expected_raises):
    """Test how normalize_lc function works for arrays of positive integers."""
    from lcanalyzer.models import normalize_lc
    import pandas.testing as pdt
    if expected_raises is not None:
        with pytest.raises(expected_raises):
            pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)
    else:
        pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)