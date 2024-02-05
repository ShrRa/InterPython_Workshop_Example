# some utility functions
import numpy as np

def is_number(x):
  return isinstance(x, (int, float, complex))

def is_list(x):
  return isinstance(x, list)

def is_array(x):
  return isinstance(x, np.ndarray)


def check_is_ndarray(data):
  if not isinstance(data, np.ndarray):
    if isinstance(data, list):
      data = np.array(data)
    if isinstance(data, (int, float, complex)):
      data = np.array([data])
  return data

# A class to contain a single-band lightcurve of an astrophysical object

class LightCurve:
  """
  A class representing a light curve.
  """

  def __init__(self, name):
    """
    Initializes a LightCurve object - requires an object name.

    Args:
      name: the name of the object (e.g. Vega)
      mjd: A vector of Modified Julian Dates (x values).
      magnitude: A vector of luminosities (y values).
      dmagnitude: A vector of luminosities uncertainties.
    """
    self.name = name
    self.mjd = np.array([])
    self.magnitude = np.array([])
    self.dmagnitude = np.array([])



  def add_observations(self, mjd, magnitude, mag_error):
    """
    Adds observations to the light curve.

    Args:
      mjd: A vector of Modified Julian Dates (x values).
      magnitude: A vector of luminosities (y values).
      mag_error: A vector of luminosities uncertainties.
    """
    mjd = check_is_ndarray(mjd)
    magnitude = check_is_ndarray(magnitude)
    mag_error = check_is_ndarray(mag_error)

    assert mjd.shape == magnitude.shape == mag_error.shape, "observations "\
    "mjd, magnitude, and errors must have the same size"
    self.mjd = np.concatenate([self.mjd, mjd])
    self.magnitude = np.concatenate([self.magnitude, magnitude])
    self.dmagnitude = np.concatenate([self.dmagnitude, mag_error])

  def __str__(self):
    # the __str__ method of a class determins what is shown if you print the class instance.
    # In this case it makes sense to show the data points
    _ = self.name + "\nmjd\t mag\t magerr\n"
    for datapoint in zip(self.mjd, self.magnitude, self.dmagnitude):
      _ = _ + "\t".join([str(datapoint[0]), str(datapoint[1]), str(datapoint[2])]) + "\n"
    return _


class Supernova(LightCurve):
  """
  A class representing a supernova light curve.
  A supernova is a kind of time-varying astrophysical object so it inherits the generic lightcurve class
  """

  def __init__(self, name, mjd=[], magnitude=[], magnitude_errors=[],
               peak_mjd=np.nan, peak_magnitude=np.nan):
    """    Initializes a Supernova object.

    Args:
      name: supernova name
      mjd: A vector of Modified Julian Dates (x values).
      magnitude: A vector of luminosities (y values).
      dmagnitude: A vector of luminosities uncertainties.
      peak_mjd: The MJD of the peak luminosity.
      peak_magnitude: The peak luminosity.
    """
    super().__init__(name)
    super().add_observations(mjd, magnitude, magnitude_errors)

    self.standard_subtypes = ["Ia", "IIl", "IIp", "SNIax", "IIb", "Ibc",
                              "Ib", "Ibn", "Ic", "Ic-bl"]
    self.set_peak(peak_mjd, peak_magnitude)

  def set_peak(self, peak_mjd, peak_magnitude):
    self.peak_mjd = peak_mjd
    self.peak_magnitude = peak_magnitude

  def set_sntype(self, sntype):
    if not sntype in self.standard_subtypes:
      import warnings
      warnings.warn("Warning: either this is an unusual supernova "
			"or the type has been entered in a non standard way "
			"available standard types are:" + " ".join(self.standard_subtypes))
    self.sntype = sntype



