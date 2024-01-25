"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

def test_mean_mag_zeros():
    from lightcurves.models import mean_mag

    test_input = {'a':np.array([0, 0, 0]), 'b':np.array([0, 0, 0])}
    test_result = 0

    npt.assert_array_equal(mean_mag(test_input, 'a'), test_result)

def test_mean_mag_integers():
    from lightcurves.models import mean_mag

    test_input = {'a':np.array([1, 2, 3]), 'b':np.array([4, 5, 6])}
    test_result = 2

    npt.assert_array_equal(mean_mag(test_input, 'a'), test_result)


def test_max_mag():
    from lightcurves.models import max_mag

    test_input = {'a':np.array([0, 1, 2]), 'b':np.array([3, 4, 5])}
    test_result = 5

    npt.assert_array_equal(max_mag(test_input, 'b'), test_result)

def test_min_mag():
    from lightcurves.models import min_mag

    test_input = {'a':np.array([0, 1, 2]), 'b':np.array([3, 4, 5])}
    test_result = 3

    npt.assert_array_equal(min_mag(test_input, 'b'), test_result)
    
'''
def test_find_peak_1D():
    from lightcurves.models import find_peak

    test_input = np.array([0, 0, 1, 0, 0])
    test_result = 2

    npt.assert_array_equal(find_peak(test_input), test_result)

def test_find_peak_2D():
    from lightcurves.models import find_peak

    test_input = np.arange(6).reshape(3,2)
    test_result = np.array([2, 2])

    npt.assert_array_equal(find_peak(test_input, axis=0), test_result)


def test_calc_period():
    """Test that Lomb-Scargle period function returns the period of a sine wave to within 5 decimal places"""
    from lightcurves.models import calc_period
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
    from lightcurves.models import calc_period
    from astropy import units as u

    test_array = np.arange(0, 1000, 0.001) * u.day
    test_input = np.zeros_like(test_array)
    test_min_freq = 2.0 * (1 / u.day)
    test_max_freq = 5.0 * (1 / u.day)

    test_result = calc_period(test_array, test_input, min_freq_search=test_min_freq, max_freq_search=test_max_freq).value
    
    npt.assert_array_equal(1 / test_min_freq.value, test_result)
'''