"""Module containing code for plotting a lightcurve."""

from matplotlib import pyplot as plt
    
def plotUnfolded(mjds,mags,mjd_label='Mjd (days)',mag_label='Mag',color='blue',marker='o'):
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
        mjds,
        mags,
        color=color,
        marker=marker
    )
    ax.minorticks_on()
    ax.set_xlabel(mjd_label)
    ax.set_ylabel(mag_label)
    fig.tight_layout()
    plt.show()

