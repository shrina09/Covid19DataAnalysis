import sys
import csv

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
# python graphing_mental_health_cases.py graphing_file.csv IDs.pdf

import numpy as np 
import matplotlib.pyplot as plt
#  matplotlib are for plotting.  The matplotlib
# library is the actual graphics library.


def main(argv):

  
  if len(argv) != 3:
        print("Usage:",
              "create_ON_phu_cases_plot.py <data file> <graphics file>")
        sys.exit(-1)


  csv_filename = argv[1]
  graphics_filename = argv[2]

  
  try:
    file_fh = open(csv_filename, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open names file '{}' : {}".format(csv_filename, err),   
           file=sys.stderr)
    sys.exit(1)

  
  fileReader = csv.reader(file_fh)

  fig = plt.figure()

     
  depressive_cases = [] #deprresood
  anxiety_cases = [] #anxiety
  index = [] #age #+ year

  next(fileReader)
  for row_data_fields in fileReader:
      
    depressive_cases.append(int(row_data_fields[0]))
    anxiety_cases.append(int(row_data_fields[1]))
    index.append(row_data_fields[3] + "\n" + " (" + row_data_fields[2] + ")")

    # print("depression", depressive_cases)
    # #print(type(depressive_cases))
    # print("anxiety", anxiety_cases)
    # #print(type(anxiety_cases))
    # print(index)
    # #print(type(index))

  # plt.bar(index, anxiety_cases)

  plt.xlabel("Age-range by Year")
  plt.ylabel("% of Cases")
  plt.title("Proportion of Positive Screens for Major Depressive Disorder and Generalized Anxiety Disorder")
  # plt.show()

  # df = pd.DataFrame({'anxiety': anxiety_cases, 'depression': depressive_cases}, index=index)
  # ax = df.plot.bar(rot=0)
  X_axis = np.arange(len(index))


  #X = np.arange(4)
  #fig = plt.figure()
  # ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])
  plt.bar(X_axis - 0.2, depressive_cases , 0.4, label="depression")
  plt.bar(X_axis + 0.2, anxiety_cases, 0.4, label="anxiety")

  plt.xticks(X_axis, index)
  plt.legend()

  

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
  fig.savefig(graphics_filename, bbox_inches="tight")


  plt.show()
  

    
main(sys.argv)


# https://youtu.be/ZjQCPMO7LBE

