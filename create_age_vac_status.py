 
# python create_age_vac_status.py 2021 09 13 2022 03 19 cases_by_age_vac_status.csv 60-79

import csv
import sys
import datetime



# Main function
def main(argv):
    #There need to be 9 arguements specifically
    if len(argv) != 9:
        print("Usage: read_file.py <file name>")

# It should take the following arguments on its command line:
#storing arguements up to 7
    year_start = argv[1]
    month_start = argv[2]
    day_start = argv[3]
    year_end = argv[4]
    month_end = argv[5]
    day_end = argv[6]
    fileName = argv[7]
    age = argv[8]

    if age.find("yrs") > 0: 
      age= age.replace('yrs', '')
          
    if age.find("-") > 0: 
      #split
      age = int(age.replace('-', ''))
    #if the index occurrence of + is greater than 0
    elif age.find("+") > 0: 
      age = int(age.replace('+', ''))
      #if the index occurrence of - is greater than 0
      #split
      # age = int(age.split("+")[0])

    #print(type(age))
    #print(age)
  
    year_start_comp = int(year_start)
    year_end_comp = int(year_end)

    #Correct format for date

    #Adding a 0 when it doesen't have a 0 so we can later convert it to a date time object

    # if year is in 2021 or 2022
    if (year_start_comp < 2021 or year_start_comp > 2022):
        #print statement
        print("Please enter 2021 or 2022 for start year")
        #exit statement
        sys.exit(1)
# if year is in 2021 or 2022
    if (year_end_comp < 2021 or year_end_comp > 2022):
        #print statement
        print("Please enter 2021 or 2022 for the end year")
        #sys exit
        sys.exit(1)

#if length is not 2 (for arguement)
    if (len(day_start) != 2):
        day_start = "0" + day_start
#if length is not 2 (for arguement)
    if (len(day_end) != 2):
        day_end = "0" + day_end
#if length is not 2 (for arguement)
    if (len(month_start) != 2):
        month_start = "0" + month_start
#if length is not 2 (for arguement)
    if (len(month_end) != 2):
        month_end = "0" + month_end

#formatting start date with dashes and end date
    startDate = year_start + "-" + month_start + "-" + day_start
    endDate = year_end + "-" + month_end + "-" + day_end

    #start and end date converter
    startDateConv = datetime.date.fromisoformat(startDate)
    endDateConv = datetime.date.fromisoformat(endDate)

    #print(startDateConv)
    #print(endDateConv)
    #printing them

  #date, %ICU-Unvacinated, %ICU-fullVacinated
    print("DATE,% OF ICU_CASES,VACCINE_STATUS")

    #trying to open file
    try:
        file_fh = open(fileName, encoding="utf-8-sig")
    #if it cannot be opened notify
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(fileName, err),
              file=sys.stderr)
        #exiting
        sys.exit(1)
      

    #variable for reading of the opened file
    fileReader = csv.reader(file_fh)
    #opening file for writing

    with open('graphing_file.csv', 'w') as file:
      writer = csv.writer(file)
      # categories
      line1 = ["DATE", "% OF ELDERLY_CASES", "VACCINE_STATUS"]
      writer.writerow(line1)
      checker = False
      next(fileReader)
      
      #for row date in file reader
      for row_data_fields in fileReader:
        #formatting
        convertDate = datetime.date.fromisoformat(row_data_fields[0])
        #declaring variable
        age_file = row_data_fields[1]


        check = 0
        #removing all extras other than the number so we can convert it to integer later
        
        if age_file == "ALL":
          age_file = int('0');
          check = 1
          
        if check != 1 and age_file.find("yrs") > 0: 
          age_file = age_file.replace('yrs', '')
          
        if check != 1 and age_file.find("-") > 0: 
      #replacing dashes with nothing
          age_file = int(age_file.replace('-', ''))
          
    #if the index occurrence of + is greater than 0
        elif check != 1 and age_file.find("+") > 0: 
          age_file = int(age_file.replace('+', ''))

        # print(type(age_file))
        #print(age_file)
       # if convert date is = to startDate
        # print(f"age '{age}' age_file '{age_file}'")
        if convertDate == startDateConv and age == age_file:
          row1 = [row_data_fields[0],row_data_fields[2],"UNVACCINATED_CASES"]
          row2 = [row_data_fields[0],row_data_fields[5],"FULLY_VACCINATED_CASES"]
          #writing rows for both 
          writer.writerow(row1)
          writer.writerow(row2)
          
          print('{},{},{}'.format (row_data_fields[0], row_data_fields[2],"UNVACINATED_CASES"))
          #printing for Vac_cases
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[5],"FULLY_VACCINATED_CASES"))
  
          checker = True
          
          #if the checker is 
        if checker == True and convertDate != startDateConv and age == age_file:
      
          row1 = [row_data_fields[0], row_data_fields[2], "UNVACCINATED_CASES"]
          row2 = [row_data_fields[0], row_data_fields[5],"FULLY_VACCINATED_CASES"]
                  #writing rows for both 
          writer.writerow(row1)
          writer.writerow(row2)
          
          print('{},{},{}'.format (row_data_fields[0], row_data_fields[2],"UNVACCINATED_CASES"))
                #printing for Vac_cases
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[5],"FULLY_VACCINATED_CASES"))
              #once it conv date reaches the last date then exit the program because were finished

        # if convertDate == endDateConv:
        #     sys.exit(1)
        # lastDate = "2021-10-24"
        # lastDateConv = datetime.date.fromisoformat(lastDate)

        # if lastDate < endDateConv:
        #    if lastDateConv == convertDate:
        #       sys.exit(1)
             
      if convertDate == endDateConv and age == age_file:
        sys.exit(1)
        #file.seek(0, os.SEEK_END)
        


            
#calling the main function
main(sys.argv)

# take out the dashes from the intial input 
# and from row_data_fields[0]
#   convert it to an int and compare


# if 2021-10-23 < end_date: 
#   if 2021-10-23 == convertDate and age != 60:
#     exit
# elif convert_date == end_date:
#   exit

# if age is nit 60: 
#    do the for loop we have

# if age is 60 
#   do for loop that we had 