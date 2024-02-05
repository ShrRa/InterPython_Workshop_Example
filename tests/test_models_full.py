"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest
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

def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output

# Parametrization for max_mag function testing
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


def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)

def test_min_mag_negatives():
    # Test that min_mag function works for negatives
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[-7, -7, -3], 
                                       [-4, -3, -1], 
                                       [-1, -5, -3]], columns=list("abc"))
    test_input_colname = "b"
    test_output = -7

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_negatives():
    # Test that mean_mag function works for negatives
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[-7, -7, -3], 
                                       [-4, -3, -1], 
                                       [-1, -5, -3]], columns=list("abc"))
    test_input_colname = "a"
    test_output = -4.

    assert mean_mag(test_input_df, test_input_colname) == test_output


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
        #pd.Series(data=[np.NaN,np.NaN,np.NaN,np.NaN])),
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
    from lcanalyzer.models_full import normalize_lc
    import pandas.testing as pdt
    if expected_raises is not None:
        with pytest.raises(expected_raises):
            pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)
    else:
        pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)

'''
# Parametrization for normalize_lc function testing without ValueError
@pytest.mark.parametrize(
    "test_input_df, test_input_colname, expected",
    [
        (pd.DataFrame(data=[[8, 9, 1], 
                            [1, 4, 1], 
                            [1, 2, 4], 
                            [1, 4, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[1,0.285,0,0.285])),
        (pd.DataFrame(data=[[1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1], 
                            [1, 1, 1]], 
                      columns=list("abc")),
        "b",
        pd.Series(data=[0.,0.,0.,0.])),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        #pd.Series(data=[np.NaN,np.NaN,np.NaN,np.NaN])),
         pd.Series(data=[0.,0.,0.,0.])),
    ])
def test_normalize_lc(test_input_df, test_input_colname, expected):
    """Test how normalize_lc function works for arrays of positive integers."""
    from lcanalyzer.models_full import normalize_lc
    import pandas.testing as pdt
    pdt.assert_series_equal(normalize_lc(test_input_df,test_input_colname),expected,check_exact=False,atol=0.01,check_names=False)

    

def test_find_peak_1D():
    from lcanalyzer.models import find_peak

    test_input = np.array([0, 0, 1, 0, 0])
    test_result = 2

    npt.assert_array_equal(find_peak(test_input), test_result)

def test_find_peak_2D():
    from lcanalyzer.models import find_peak

    test_input = np.arange(6).reshape(3,2)
    test_result = np.array([2, 2])

    npt.assert_array_equal(find_peak(test_input, axis=0), test_result)


def test_calc_period():
    """Test that Lomb-Scargle period function returns the period of a sine wave to within 5 decimal places"""
    from lcanalyzer.models import calc_period
    from astropy import units as u

    test_period = 0.5
    test_array = np.arange(0, 1000, 0.001) * u.day
    test_input = np.sin(test_array.value * np.pi * 2 / test_period)
    test_min_freq = 1.0 * (1 / u.day)
    test_max_freq = 3.0 * (1 / u.day)

    test_result = calc_period(test_array, test_input, min_freq_search=test_min_freq, max_freq_search=test_max_freq).value
    
    npt.assert_almost_equal(test_period, test_result, decimal = 5)

def test_calc_period_zeros():
    """Test that Lomb-Scargle period function returns the reciprocal of test_min_freq for an array of all zeros"""
    from lcanalyzer.models import calc_period
    from astropy import units as u

    test_array = np.arange(0, 1000, 0.001) * u.day
    test_input = np.zeros_like(test_array)
    test_min_freq = 2.0 * (1 / u.day)
    test_max_freq = 5.0 * (1 / u.day)

    test_result = calc_period(test_array, test_input, min_freq_search=test_min_freq, max_freq_search=test_max_freq).value
    
    npt.assert_array_equal(1 / test_min_freq.value, test_result)
'''