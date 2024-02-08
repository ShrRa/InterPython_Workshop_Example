"""Module containing code for plotting a lightcurve."""

from matplotlib import pyplot as plt

def plot_unfolded(mjds, mags, mjd_label, mag_label, color, marker):
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
