"""Tests for statistics functions within the Model layer."""

import pandas as pd
import numpy as np

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_nans():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [np.nan, 4, 1]], columns=list("abc"))
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


def test_min_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 1

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_nans():
    # Test that max_mag function works for integers
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [np.nan, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 1

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 11/3.
    

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_nans():
    # Test that max_mag function works for integers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [np.nan, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 2.0
    

    assert mean_mag(test_input_df, test_input_colname) == test_output
    

def test_mean_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import mean_mag

    

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_calc_stat_integers():
    from lcanalyzer.models import calc_stat
    df1 = pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc"))
    df2 = pd.DataFrame(data=[[7, 3, 2], [8, 4, 2], [5, 6, 4]], columns=list("abc"))
    df3 = pd.DataFrame(data=[[2, 6, 3], [1, 3, 6], [8, 9, 1]], columns=list("abc"))
    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = {"df1_max": 8, "df2_max": 6, "df3_max": 9}
    assert  calc_stat(test_input, ["df1", "df2", "df3"], "b") == test_output

def test_calc_stat_zeros():
    from lcanalyzer.models import calc_stat
    df1 = pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc"))
    df2 = pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc"))
    df3 = pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], columns=list("abc"))
    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = {"df1_max": 0, "df2_max": 0, "df3_max": 0}
    assert  calc_stat(test_input, ["df1", "df2", "df3"], "b") == test_output

def test_calc_stat_nans():
    from lcanalyzer.models import calc_stat
    df1 = pd.DataFrame(data=[[1, np.nan, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc"))
    df2 = pd.DataFrame(data=[[7, 3, 2], [8, np.nan, 2], [5, 6, 4]], columns=list("abc"))
    df3 = pd.DataFrame(data=[[2, 6, 3], [1, np.nan, 6], [8, 9, 1]], columns=list("abc"))
    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = {"df1_max": 8, "df2_max": 6, "df3_max": 9}
    assert  calc_stat(test_input, ["df1", "df2", "df3"], "b") == test_output

def test_calc_stat_stats():
    from lcanalyzer.models import calc_stat
    df1 = pd.DataFrame(data=[[1, 5, 3], [7, 8, 9], [3, 4, 1]], columns=list("abc"))
    df2 = pd.DataFrame(data=[[7, 3, 2], [8, 4, 2], [5, 6, 4]], columns=list("abc"))
    df3 = pd.DataFrame(data=[[2, 6, 3], [1, 3, 6], [8, 9, 1]], columns=list("abc"))
    test_input = {"df1": df1, "df2": df2, "df3": df3}
    test_output = {"df1_mean": 17/3., "df2_mean": 13/3., "df3_mean": 6}
    assert  calc_stat(test_input, ["df1", "df2", "df3"], "b", stat='mean') == test_output