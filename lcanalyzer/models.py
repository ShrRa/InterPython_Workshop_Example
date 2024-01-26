"""Module containing models representing lightcurves.

The Model layer is responsible for the 'business logic' part of the software.

The lightcurves are saved in a table (2D array) where each row corresponds to a single observation. 
Depending on the dataset (LSST or Kepler), a table can contain observations of a single or several objects, 
in a single or different bands.
"""

import pandas as pd
import numpy as np
from astropy.timeseries import LombScargle

def load_dataset(filename):
    """Load a table from CSV file.
    
    :param filename: The name of the .csv file to load
    :returns: pd.DataFrame with the data from the file.
    """
    return pd.read_csv(filename)


def mean_mag(data,mag_col):
    """Calculate the mean magnitude of a lightcurve"""
    return np.mean(data[mag_col], axis=0)


def max_mag(data,mag_col):
    """Calculate the max magnitude of a lightcurve"""
    return data[mag_col].max()


def min_mag(data,mag_col):
    """Calculate the min magnitude of a lightcurve
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The min value of the column.
    """
    return data[mag_col].min()

'''
def find_peak(input, axis=None):
    """Return the indices of the maximum values along an axis
    
    :param input: Input array
    """
    return np.argmax(input, axis)

def calc_period(t, y, min_freq_search, max_freq_search):
    """Calculate the period corresponding to the highest-power 
       frequency returned by astropy.timeseries.LombScargle

    :param array-like or `~astropy.units.Quantity` t: 
        sequence of observation times
    :param array-like or `~astropy.units.Quantity` y: 
        sequence of observations associated with times t
    :param float or `~astropy.units.Quantity` min_freq_search: 
        If specified, then use this minimum frequency rather than one
        chosen based on the size of the baseline. Should be `~astropy.units.Quantity`
        if inputs to LombScargle are `~astropy.units.Quantity`.
    :param float or `~astropy.units.Quantity` max_freq_search: 
        If specified, then use this maximum frequency rather than one
        chosen based on the average nyquist frequency. Should be `~astropy.units.Quantity`
        if inputs to LombScargle are `~astropy.units.Quantity`.
    :return float Period
    """
    
    frequency, power = LombScargle(t,y).autopower(minimum_frequency=min_freq_search,
                                                  maximum_frequency=max_freq_search)
    
    # find the index with maximum power (= peakbin)
    peakbin = find_peak(power)

    peak_freq = frequency[peakbin]

    return 1.0 / peak_freq
'''
