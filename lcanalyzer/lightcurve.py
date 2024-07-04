import pandas as pd
import numpy as np

class Lightcurve:
    """Class Lightcurve"""

    def __init__(self, mjds=None, mags=None, mag_errs=None):
        self.lc = {}
        if mjds is not None:
            self.add_observations(mjds, mags, mag_errs)

    def add_observations(self, mjds, mags, mag_errs=None):
        """
        Adds observations to the light curve.
        
        Args:
         mjds: A vector of Modified Julian Dates (x values).
         mags: A vector of luminosities (y values).
         mag_errs: A vector of magnitude errors.
        """
        self.lc["mjd"] = self.convert_to_array(mjds)
        self.lc["mag"] = self.convert_to_array(mags)
        if mag_errs is not None:
            self.lc["mag_errs"] = self.convert_to_array(mag_errs)
        self.compare_len(self.lc.values())
        return self.lc

    def convert_to_array(self,data):
        """ Check if the data is iterable and convert it into np.array, otherwise raise an exception

        Args:
        :parem data: lightcurve data to convert into an array
        :return: data converted to an np.array
        :raises: ValueError if the data is not iterable.
        """
        if not isinstance(data, np.ndarray):
            if isinstance(data, (list,tuple,pd.Series)):
                data = np.array(data)
            elif isinstance(data, (int, float)):
                data = np.array([data])
            else:
                raise ValueError("The data type of the input is incorrect!")
        return data

    def compare_len(self,arrs):
        """ Check that all arrays are of the same length

        Args:
        :parem arrs: list of arrays
        :return: None
        :raises: ValueError if arrays have different lengths.
        """
        lens = [len(arr) for arr in arrs]
        if len(set(lens)) > 1: # set() turns an iterable into a set of unique values.
        # If the values are all the same, the set will contain only one element
            raise ValueError("Passed timestamps and mags or mag_errs arrays have different lengths!")
        return

    @property
    def mean_mag(self):
        """ Calculates the mean magnitude from object's data

        Args:
        :return: a float for the mean magnitude
        """
        return np.mean(self.lc["mags"])

    def __len__(self):
        return len(self.lc["mjds"])
