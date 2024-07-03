# import modules
import argparse
from lcanalyzer import survey, plots

def main():
    """The MVC Controller of the LSST data table.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infile = args.infile
    lsst = survey.Survey(infile)

    if args.info == 'unique':
        print(lsst.unique_objects)

    if args.info == 'plotFirst':
        obj_id = lsst.unique_objects[0]
        band = args.band
        time_col = 'mjds'
        mag_col = 'mags'
        lc = lsst.get_lc(obj_id, band)
        plots.plotUnfolded(lc[time_col],lc[mag_col])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A package for inspecting LSST survey tables containing variability observations')

    parser.add_argument('infile',
                        help='Input CSV or PKL file containing LSST light curves')

    parser.add_argument(
        '--info',
        default='unique',
        choices=['unique', 'plotFirst'],
        help='Which info should be displayed?')

    parser.add_argument(
        '--band',
        type=str,
        default='g',
        help='Which band should be plotted?')

    args = parser.parse_args()
    
    main()
