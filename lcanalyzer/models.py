"""Module containing models representing lightcurves.

The Model layer is responsible for the 'business logic' part of the software.

The lightcurves are saved in a table (2D array) where each row corresponds to a single observation. 
Depending on the dataset (LSST or Kepler), a table can contain observations of a single or 
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
    
    :param data: input data
           mag_col: Name of the column in the data file
    :returns: mean of the mag_col column of the data file
    """
    return data[mag_col].mean()


def max_mag(data, mag_col):
    """Calculate the max magnitude of a lightcurve.
    
    :param data: input data
           mag_col: Name of the column in the data file
    :returns: max of the mag_col column of the data file
    """
    return data[mag_col].max()


def min_mag(data,mag_col):
    """Calculate the min magnitude of a lightcurve
    :param data: pd.DataFrame with observed magnitudes for a single source.
    :param mag_col: a string with the name of the column for calculating the min value.
    :returns: The min value of the column.
    """
    return data[mag_col].min()

### Get maximum values for all bands.
def calc_stat(lc, bands, mag_col, stat = 'max'):
    stats = {
        'max':max_mag,
        'min':min_mag,
        'mean':mean_mag}
    # Define an empty dictionary where we will store the results
    stat_output = {}
    # For each band get the maximum value and store it in the dictionary
    for b in bands:
        stat_output[b + "_"+stat] = stats[stat](lc[b], mag_col)
    return stat_output

def normalize_lc(df, mag_col):
    # Normalize a light curve
    if any(df[mag_col].abs() > 90):
        raise ValueError(mag_col + " contains values with abs() larger than 90!")
    min_data = min_mag(df, mag_col)
    max_data = max_mag((df - min_data), mag_col)
    lc = (df[mag_col] - min_data) / max_data
    lc = lc.fillna(0)
    return lc