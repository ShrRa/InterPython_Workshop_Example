# Introduction

This is a template software project repository used by the [Intermediate Python for Astronomical Software Development](https://shrra.github.io/python-intermediate-development/index.html).

## LcAnalyzer
![Continuous Integration build in GitHub Actions](https://github.com/<your_github_username>/light-curve-analysis/workflows/CI/badge.svg?branch=main)
LcAnalyzer is a package written in Python that allows you to inspect light curves.

### Main features
Here are some key features of LcAnalyzer:

- Reading CSV and Pickle files;
- Giving the list of unique objects present in the data;
- Selecting observations of a given star in a given bands;

### Prerequisites
LcAnalyzer requires the following Python packages:

- [Pandas](https://pandas.pydata.org/) - makes use of Pandas's data types and statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run LcAnalyzer's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - LcAnalyzer's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Purpose

This repository is intended to be used as a code template which is copied by learners at [Intermediate Python for Astronomical Software Development](https://shrra.github.io/python-intermediate-development/index.html) course.
This can be done using the `Fork` button towards the top right of this repo's GitHub page.

This software project is not finished, is currently failing to run and contains some code style issues. It is used as a starting point for the course - issues will be fixed and code will be added in a number of places during the course by learners in their own copies of the repository, as course topics are introduced.

## Data

Two datasets are available in `data/directory`. 

One dataset is `kepler_RRLyr.csv`, which contains information on a single variable source from the Kepler space telescope. The columns within this dataset are
- time
- flux
- flux_err
- quality
- timecorr
- centroid_col
- centroid_row
- cadenceno
- sap_flux
- sap_flux_err
- sap_bkg
- sap_bkg_err
- pdcsap_flux
- pdcsap_flux_err
- sap_quality
- psf_centr1
- psf_centr1_err
- psf_centr2
- psf_centr2_err
- mom_centr1
- mom_centr1_err
- mom_centr2
- mom_centr2_err
- pos_corr1
- pos_corr2

The other dataset is `lss_RRLyr.pkl`, which contains simulated data of 25 variable sources, using the LSST Data Preview 0. The columns within this dataset are
- band
- ccdVisitId
- coord_ra
- coord_dec
- objectId
- psfFlux
- psfFluxErr
- psfMag
- ccdVisitId2
- band2
- expMidptMJD
- zeroPoint

## Tests

Several tests have been implemented already, some of which are currently failing.
These failing tests set out the requirements for the additional code to be implemented during the workshop.
