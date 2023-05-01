# An example command line to run this code
# python create_cases_mental_health.py 18-24 65+ Mental_Health.csv 
import csv
import sys


def main(argv):
  #There need to be 4 arguements specifically
  if len(argv) != 4:
    print("Usage: read_file.py <file name>")

#Taking in 3 arguements and storing them as variables
  age_start = argv[1]
  age_end = argv[2]
  file_name = argv[3]

  #if the index occurrence of - is greater than 0
  if age_start.find("-") > 0: 
    #split
    age_start = int(age_start.split("-")[0])
  #if the index occurrence of + is greater than 0
  elif age_start.find("+") > 0: 
    age_start = int(age_start.split("+")[0])
  #if the index occurrence of - is greater than 0
  if age_end.find("-") > 0: 
    #split
    age_end = int(age_end.split("-")[0])
  #if the index occurrence of + is greater than 0
  elif age_end.find("+") > 0: 
    #split
    age_end = int(age_end.split("+")[0])

#openfile and catch it if the file didnt open
  try:
    file_fh = open(file_name, encoding="utf-8-sig")
#Explaining to the user that the file did not open 
  except IOError as err:
    print("Unable to open names file '{}' : {}".format(file_name, err),   
           file=sys.stderr)
    #stopping system if file does not open 
    sys.exit(1)

#storing reader of opened file into variable
  fileReader = csv.reader(file_fh)


#opening file for writing, as file
  with open('graphing_file.csv', 'w',) as file:
    
    writer = csv.writer(file)
    #categories 
    line1 = ["DEPRESSIVE_DISORDER","ANXIETY_DISORDER","YEAR","AGE_RANGE"]
    #printing category names
    print("DEPRESSIVE_DISORDER,ANXIETY_DISORDER,YEAR,AGE_RANGE")
    #writing a row for line 1
    writer.writerow(line1)
    
    next(fileReader)
    #for the row data in the file reader
    for row_data_fields in fileReader:
      #if the index occurrence of - is greater than 0
      if row_data_fields[3].find("-") > 0: 
        #split
        range_start= int(row_data_fields [3].split("-")[0])
      #if the index occurrence of + is greater than 0
      elif row_data_fields[3].find("+") > 0: 
        #split
        range_start= int(row_data_fields [3].split("+")[0])
      #if int range_start is >= age_start and range start is <= age_end
      if range_start >= age_start and range_start <= age_end:
        #storing row data feilds in list
        row = [row_data_fields[0], row_data_fields[1], row_data_fields[2], row_data_fields[3]]
        #printing out in order with formatting
        print('{},{},{},{}'.format(row_data_fields[0], row_data_fields[1], row_data_fields[2], row_data_fields[3]))
        #writing a row in row
        writer.writerow(row)
        
      if age_end == row_data_fields[3]:
        print("Reached the end")
      
#calling the main
main(sys.argv)