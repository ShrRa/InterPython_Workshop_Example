# LcAnalyzer
![Continuous Integration build in GitHub Actions](https://github.com/<your_github_username>/light-curve-analysis/workflows/CI/badge.svg?branch=main)
LcAnalyzer is a package written in Python that allows you to inspect light curves.

## Main features
Here are some key features of LcAnalyzer:

- Reading CSV and Pickle files;
- Giving the list of unique objects present in the data;
- Selecting observations of a given star in a given bands;
...

## Prerequisites
LcAnalyzer requires the following Python packages:

- [Pandas](https://pandas.pydata.org/) - makes use of Pandas's data types and statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run LcAnalyzer's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - LcAnalyzer's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

