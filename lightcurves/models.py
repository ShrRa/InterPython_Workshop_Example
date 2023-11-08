"""Module containing models representing lightcurves.

The Model layer is responsible for the 'business logic' part of the software.

The lightcurves are saved in a table (2D array) where each row corresponds to a single observation. 
Depending on the dataset (LSST or Kepler), a table can contain observations of a single or several objects, 
in a single or different bands.
"""

import pandas as pd


def load_dataset(filename):
    """Load a table from CSV file.

    :param filename: The name of the file to load
    """
    return pd.read_csv(filename)


def mean_mag(data,magCol):
    """Calculate the mean magnitude of a lightcurve."""
    return data[magCol].mean()


def daily_max(data,magCol):
    """Calculate the max magnitude of a lightcurve."""
    return data[magCol].max()


def daily_min(data,magCol):
    """Calculate the min magnitude of a lightcurve."""
    return data[magCol].min()