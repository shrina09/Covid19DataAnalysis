
#
#   Packages and modules
#
import sys

# python graphing_create_vac_rate.py graphing_file.csv IDs.pdf


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
        csv_df1 = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    # try:
    #   csv_df2 = pd.read_csv(csv_filename2)

    # except IOError as err:
    #     print("Unable to open source file", csv_filename2,
    #             ": {}".format(err), file=sys.stderr)
    #     sys.exit(-1)



    # You can always print out a data frame if you want to see what is in it
    # though if it is huge, this is not a good idea)
    print(csv_df1)
    # print(csv_df2)


    # At this point in the file, we begin to do the plotting


    fig = plt.figure()


    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure. 

    plt.title("Rate Of Hospitalized Cases And Covid-19 Cases Among Vaccinated And Unvaccinated Individuals")

    #DATE,CASES_FULL_VAC_RATE_7MA,CASES_UNVAC_RATE_7MA
    #DATE,RATE OF HOSPITAL_NON_ICU_UNVAC,RATE OF HOSPITAL_NON_ICU_FULL_VAC
  
    ax1 = sns.lineplot(x = "DATE", y = "RATE_OF_CASES",hue = "STATUS", data=csv_df1)
    # ax2 = sns.lineplot(x = "DATE", y = "RATE_OF_CASES",hue = "VACCINE_HOSPITAL_STATUS_NON_ICU", data=csv_df2)
    # ax2 = sns.lineplot(x = "DATE", y = "CASES_UNVAC_RATE_7MA", label = "Vaccinated", data=csv_df1)
    # ax21 = sns.lineplot(x = "DATE", y = "RATE OF HOSPITAL_NON_ICU_FULL_VAC",label = "Hospitiliazed Unvaccinated", data=csv_df2)
    # ax22 = sns.lineplot(x = "DATE", y = "RATE OF HOSPITAL_NON_ICU_UNVAC" ,label = "Hospitiliazed Vaccinated", data=csv_df2)


    ax1.xaxis.set_major_locator(ticktools.MaxNLocator(8))
    # ax2.xaxis.set_major_locator(ticktools.MaxNLocator(8))
    # ax21.xaxis.set_major_locator(ticktools.MaxNLocator(8))
    # ax22.xaxis.set_major_locator(ticktools.MaxNLocator(8))


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
# we need 4 different lines with different colours 
#date as the x-axis
#y-axis is the rate of cases in ICU and cases of covid (rate of cases)
