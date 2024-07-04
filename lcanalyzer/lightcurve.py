import pandas as pd
import numpy as np

class Lightcurve:
    """Class Lightcurve"""

    def __init__(self, mjds=None, mags=None, mag_errs=None):
        self.lc = {}
        if mjds is not None:
            self.add_observations(mjds, mags, mag_errs)

    def add_observations(self, mjds, mags, mag_errs=None):
        self.lc["mjds"] = self.convert_to_array(mjds)
        self.lc["mags"] = self.convert_to_array(mags)
        if mag_errs is not None:
            self.lc["mag_errs"] = self.convert_to_array(mag_errs)
        self.compare_len(self.lc.values())
        return self.lc

    def convert_to_array(self, data):
        if not isinstance(data, np.ndarray):
            if isinstance(data, (list, tuple, pd.Series)):
                data = np.array(data)
            elif isinstance(data, (int, float)):
                data = np.array([data])
            else:
                raise ValueError("The data type of the input is incorrect!")
        return data

    def compare_len(self, arrs):
        lens = [len(arr) for arr in arrs]
        if len(set(lens)) > 1:
            raise ValueError(
                "Passed timestamps and mags or mag_errs arrays have different lengths!"
            )
        return

    @property
    def mean_mag(self):
        return np.mean(self.lc["mags"])

    def __len__(self):
        return len(self.lc["mjds"])