"""Module containing code for plotting a lightcurve."""

from matplotlib import pyplot as plt
import pandas as pd
    
def plotUnfolded(data,mag_col,time_col):
    """
    Display plots of unfolded lightcurves in different bands.
    :param data: a table of observations of a single object in a single band
    :param mag_col: the name of the column with magnitudes to plot
    :param time_col: the name of the column with time stamps
    """
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(1,1,1)
    ax.plot(data[time_col].to_numpy(), 
             data[mag_col].to_numpy(),'k.', ms=10)
    ax.minorticks_on()
    ax.set_xlabel('MJD (days)')
    ax.set_ylabel('Mag')
    fig.tight_layout()
    ax.show()