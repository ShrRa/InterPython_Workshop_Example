"""Module containing models representing lightcurves.

The Model layer is responsible for the 'business logic' part of the software.

The lightcurves are saved in a table (2D array) where each row corresponds to a single observation. 
Depending on the dataset (LSST/Kepler), a table can contain observations of a single or 
several objects, in a single or different bands.
"""

import pandas as pd

def load_dataset(filename):
    """Load a table from CSV file.
    
    :param filename: The name of the .csv file to load
    :returns: pd.DataFrame with the data from the file.
    """
    return pd.read_csv(filename)


def mean_mag(data,mag_col):
    """Calculate the mean magnitude of a lightcurve.
    
    :parem data: pandas DataFrame with observed magnitudes of single source
    :parem mag_col: a string for the name of the column to calculate the mean
    :returns: a float with the mean of the column of the given DataFrame
    """
    return data[mag_col].mean()


def max_mag(data,mag_col):
    """Calculate the max magnitude of a lightcurve.
    
    :parem data: pandas DataFrame with observed magnitudes of single source
    :parem mag_col: a string for the name of the column to calculate the max value
    :returns: a float with the max value of the column of the given DataFrame
    """
    return data[mag_col].max()


def min_mag(data,mag_col):
    """Calculate the min magnitude of a lightcurve.
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The min value of the column.
    """
    return data[mag_col].min()
