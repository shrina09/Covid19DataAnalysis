# python create_vac_rate.py 2021 08 11 2022 02 28 cases_by_vac_status.csv vac_status_hosp_icu.csv
#Fully vaccinated:	12,101,350
#Ontario Population: 14,826,276 

#python create_vac_rate.py 2021 08 11 2022 02 28 cases_by_vac_status.py vac_status_hosp_icu.csv
import csv
import sys
import datetime

# Main function
def main(argv):
  #There need to be 9 arguements specifically
    if len(argv) != 9:
      print("Usage: read_file.py <file name>")
    

# It should take the following arguments on its command line:
    year_start = argv[1]
    month_start = argv[2]
    day_start = argv[3]
    year_end =  argv[4]
    month_end = argv[5]
    day_end = argv[6]
    fileName1 = argv[7]
    fileName2 = argv[8]
#converting to integers
    year_start_comp = int (year_start)
    year_end_comp = int (year_end)

  #Correct format for date 

  #Adding a 0 when it doesen't have a 0 so we can later convert it to a date time object

  # if 2021 or 2022
    if (year_start_comp < 2021 or year_start_comp > 2022):
      print("Please enter 2021 or 2022 for start year")
      #exit
      sys.exit(1)
      
  # if 2021 or 2022
    if (year_end_comp < 2021 or year_end_comp > 2022): 
      #notify user
      print("Please enter 2021 or 2022 for the end year")
      #exit
      sys.exit(1)

    
    if (len(day_start) != 2):
      day_start = "0" + day_start
  
    if (len(day_end) != 2):
      day_end = "0" + day_end

    if (len(month_start) != 2): 
      month_start = "0" + month_start

    if (len(month_end) != 2):
      month_end = "0" + month_end

  
    startDate = year_start + "-" + month_start + "-" + day_start
    endDate = year_end + "-" + month_end + "-" + day_end
  
    #formatting
    startDateConv = datetime.date.fromisoformat(startDate) 
    endDateConv = datetime.date.fromisoformat(endDate)
  
    # print(startDateConv)
    # print(endDateConv)

  #variables 
    Vac_cases = 12101350
    Population = 14826276 
    Unvac_cases = Population - Vac_cases
  
  #date, %ICU-Unvacinated, %ICU-fullVacinated

  #try opening file
    try:
      file_fh1 = open(fileName1, encoding="utf-8-sig")
  #if it doesent work then inform user which file could not open
    except IOError as err:
      print("Unable to open names file '{}' : {}".format(fileName1, err),   
           file=sys.stderr)
      sys.exit(1)
  #try opening file
    try:
      file_fh2 = open(fileName2, encoding="utf-8-sig")
  #if it doesent work then inform user which file could not open
    except IOError as err:
      print("Unable to open names file '{}' : {}".format(fileName2, err),   
           file=sys.stderr)
      #exit
      sys.exit(1)

    #variables for both
    percent_unvac_cases = 0
    percent_fully_vac_cases = 0

#reader for both files
    fileReader1 = csv.reader(file_fh1)
    fileReader2 = csv.reader(file_fh2)
  
  
#print statement
    print("DATE,RATE_OF_CASES,VACCINE_STATUS")
    # opening cases_by_vac.csv
    with open('graphing_file.csv', 'w') as file:
      #writer variable
      writer = csv.writer(file)
      #3 aspects in one list
      line1 =["DATE","RATE_OF_CASES","STATUS"]
      writer.writerow(line1)
      checker = False

      next(fileReader1)
      #for rowdata in file reader
      for row_data_fields in fileReader1:
        convertDate = datetime.date.fromisoformat(row_data_fields[0]) 
        
        if row_data_fields[15] == '':
          row_data_fields[15] = '0'
        if row_data_fields[12] == '':
          row_data_fields[12] = '0'
          
        if convertDate == startDateConv: 
          # if row_data_fields[16] == "":
          #   row_data_fields[16] = "0"
          
          #DATE,CASES_FULL_VAC_RATE_7MA,CASES_UNVAC_RATE_7MA
          row1 = [row_data_fields[0],row_data_fields[15], "CASES_FULL_VAC_RATE"]
          row2 = [row_data_fields[0],row_data_fields[12], "CASES_UNVAC_RATE"]

          #write row
          writer.writerow(row1)
          writer.writerow(row2)
          #printing with format for full and Unvac_cases
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[15], "CASES_FULL_VAC"))
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[12], "CASES_UNVAC_RATE"))
          checker = True

             
        if checker ==True and convertDate != startDateConv:
          # if row_data_fields[16] == "":
          #   row_data_fields[16] = "0"
         #defining row 1 and 2
          row1 = [row_data_fields[0],row_data_fields[15], "CASES_FULL_VAC_RATE"]
          row2 = [row_data_fields[0],row_data_fields[12],"CASES_UNVAC_RATE"]
          
          # write rows 1 and 2
          writer.writerow(row1)
          writer.writerow(row2)
          
          #Printings cases non and full Vac_cases
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[15], "CASES_FULL_VAC_RATE"))
          print('{},{},{}'.format(row_data_fields[0], row_data_fields[12], "CASES_UNVAC_RATE"))

        # Making sure it stops if conv date = enddate  
        if convertDate == endDateConv:
          break
    
    

      #Second file 
      #with open('vac_hosp_icu.csv', 'w') as file:
      #writer = csv.writer(file)

      #line12 =["DATE","RATE_OF_CASES","VACCINE_HOSPITAL_STATUS_NON_ICU"]

      #writer.writerow(line12)
      checker2 = False

      next(fileReader2)
      for row_data_fields in fileReader2:
        convertDate = datetime.date.fromisoformat(row_data_fields[0]) 

        if row_data_fields[4] == '':
          row_data_fields[4] = '0'
        if row_data_fields[6] == '':
          row_data_fields[6] = '0'
          

        #DATE,RATE OF HOSPITAL_NON_ICU_UNVAC,RATE OF HOSPITAL_NON_ICU_FULL_VAC
        if convertDate == startDateConv: 
          #calculation to find perenctages
          percent_unvac_cases = ((int(row_data_fields[4])) / Vac_cases) * 100
          percent_fully_vac_cases = ((int(row_data_fields[6])) / Unvac_cases) * 100
           #defining row 1 and 2
          row1 = [row_data_fields[0], percent_unvac_cases, "RATE OF NON_ICU_UNVAC"]
          row2 = [row_data_fields[0], percent_fully_vac_cases, "RATE OF NON_ICU_FULL_VAC"]
          
          writer.writerow(row1)
          writer.writerow(row2)
           #printing with format for full and Unvac_cases
          print('{},{:.2e},{}'.format(row_data_fields[0], percent_unvac_cases,"RATE OF NON_ICU_UNVAC"))
          print('{},{:.2e},{}'.format(row_data_fields[0], percent_fully_vac_cases,"RATE OF NON_ICU_FULL_VAC"))
          
          checker2 = True

             
        if checker2 ==True and convertDate != startDateConv:
          # calculations to find percentages
          percent_unvac_cases = ((int(row_data_fields[4])) / Vac_cases) * 100
          percent_fully_vac_cases = ((int(row_data_fields[6])) / Unvac_cases) * 100
           #defining row 1 and 2
          row1 = [row_data_fields[0], percent_unvac_cases, "RATE OF NON_ICU_UNVAC"]
          row2 = [row_data_fields[0], percent_fully_vac_cases, "RATE OF NON_ICU_FULL_VAC"]
          #write rows for 1 and 2
          writer.writerow(row1)
          writer.writerow(row2)
           #printing with format for full and Unvac_cases
          print('{},{:.2e},{}'.format(row_data_fields[0], percent_unvac_cases,"RATE OF NON_ICU_UNVAC"))
          print('{},{:.2e},{}'.format(row_data_fields[0], percent_fully_vac_cases,"RATE OF NON_ICU_FULL_VAC"))

        
        # Making sure it stops if conv date = enddate  
        if convertDate == endDateConv:
          sys.exit(1)
       
  
  

#calling main function 
main(sys.argv)

#RATE_HOSPITAL_NON_ICU_CASES