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


def mean_mag(data, mag_col):
    """Calculate the mean magnitude of a lightcurve.

    :parem data: pandas DataFrame with observed magnitudes of single source
    :parem mag_col: a string for the name of the column to calculate the mean
    :returns: a float with the mean of the column of the given DataFrame
    """
    return data[mag_col].mean()


def max_mag(data, mag_col):
    """Calculate the max magnitude of a lightcurve.

    :parem data: pandas DataFrame with observed magnitudes of single source
    :parem mag_col: a string for the name of the column to calculate the max value
    :returns: a float with the max value of the column of the given DataFrame
    """
    return data[mag_col].max()


def min_mag(data, mag_col):
    """Calculate the min magnitude of a lightcurve.
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The min value of the column.
    """
    return data[mag_col].min()


def calc_stats(lc, bands, mag_col):
    """Calculate max, mean and min values for all bands of a light curve
    :param lc: dict of pd.DataFrame with observed data for multiple sources/observations
    :param bands: a string with the list of bands
    :parem mag_col: a string with the name of the column for calculating the max, mean, and min.
    :returns: A pd.DataFrame that records the max, mean, and min of each column passed through
    """
    stats = {}
    for b in bands:
        stat = {}
        stat["max"] = max_mag(lc[b], mag_col)
        stat["mean"] = mean_mag(lc[b], mag_col)
        stat["min"] = min_mag(lc[b], mag_col)
        stats[b] = stat
    return pd.DataFrame.from_records(stats)


def normalize_lc(df, mag_col):
    # Normalize a single light curve
    if any(df[mag_col].abs() > 90):
        raise ValueError(mag_col + " contains values with abs() larger than 90!")
    min_data = min_mag(df, mag_col)
    max_data = max_mag((df - min), mag_col)
    lc = (df[mag_col] - min_data) / max_data
    lc = lc.fillna(0)
    return lc
