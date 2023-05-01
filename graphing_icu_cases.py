
#
#   Packages and modules
#
import sys

# python graphing_icu_cases.py graphing_file.csv IDs.pdf
# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt

from matplotlib import ticker as ticktools


def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print("Usage:",
                "create_ON_phu_cases_plot.py <data file> <graphics file>")
        sys.exit(-1)
    
    csv_filename = argv[1]
    graphics_filename = argv[2]


    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)



    # You can always print out a data frame if you want to see what is in it
    # though if it is huge, this is not a good idea)
    print(csv_df)


    # At this point in the file, we begin to do the plotting


    fig = plt.figure()

    plt.title("Rate of ICU Cases Among Vaccinated and Unvaccinated Individuals")
    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    ax1 = sns.lineplot(x = "DATE", y = "% of ICU_CASES", hue = "VACCINE_STATUS", data=csv_df)


    ax1.xaxis.set_major_locator(ticktools.MaxNLocator(6))

    plt.xticks(rotation = 45, ha = 'right')

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")


    plt.show()

    #
    #   End of Function
    #



##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#