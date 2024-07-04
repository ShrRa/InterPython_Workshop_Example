from lcanalyzer.lightcurve import Lightcurve
import pandas as pd

class Survey:
    def __init__(
        self,
        filename: str,
        clean_nans: bool = True,
        id_col: str = "objectId",
        band_col: str = "band",
        time_col: str = "expMidptMJD",
        mag_col: str = "psfMag",
    ):
        """
        Initializes the Survey object by loading data from a file.

        Parameters:
            filename (str): The name of the file to load.
            clean_nans (bool): Whether to clean NaNs in the data.
            id_col (str): Column name for object IDs.
            band_col (str): Column name for bands.
            time_col (str): Column name for observation times.
            mag_col (str): Column name for magnitudes.
        """
        self.id_col = id_col
        self.band_col = band_col
        self.time_col = time_col
        self.mag_col = mag_col
        self.data = self._load_table(filename, clean_nans)
        self.unique_objects = self.data[self.id_col].unique()

    def load_table(self, filename, clean_nans = True):
        """Load a table from a CSV file.

        :parem filename: a string of the .csv file to load.
        :returns: a pd.DataFrame with the data from the file.
        """
        if filename.endswith(".csv"):
            df = pd.read_csv(filename)
        elif filename.endswith(".pkl"):
            df = pd.read_pickle(filename)
        if clean_nans == True:
            df = self.clean_table(df)
        return df

    def clean_table(self, df, nan_val='nan'):
        if nan_val == 'nan':
            filt_nan = ~((df[self.mag_col] == nan_val) | (df[self.mag_col].isnull()))
            return df[filt_nan]
        else:
            return df

    def get_obj_band_df(self, obj_id, band):
        filt_band_obj = (self.data[self.id_col] == obj_id) & (self.data[self.band_col] == band )
        return self.data[filt_band_obj]

    def get_lc(self, obj_id, band):
        df = self.get_obj_band_df(obj_id, band)
        lc = Lightcurve(mjds=df[self.time_col], mags=df[self.mag_col])
        return lc.lc
