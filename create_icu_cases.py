# python create_icu_cases.py 2021 08 11 2022 02 28 vac_status_hosp_icu.csv
#Fully vaccinated:	12,101,350
#Ontario Population: 14,826,276

#python create_icu_cases.py 2021 08 11 2022 05 28 vac_status_hosp_icu.csv

#3 imports
import csv
import sys
import datetime


# Main function
def main(argv):
    #There need to be 9 arguements specifically
    if len(argv) != 8:
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
    #printing them
    # print(startDateConv)
    # print(endDateConv)

    #stating variables for calculations to find things like rates
    Vac_cases = 12101350
    Population = 14826276
    Unvac_cases = Population - Vac_cases

    #date, %ICU-Unvacinated, %ICU-fullVacinated
    print("DATE,% of ICU_CASES,VACCINE_STATUS")

    #trying to open file
    try:
        file_fh = open(fileName, encoding="utf-8-sig")
    #if it cannot be opened notify
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(fileName, err),
              file=sys.stderr)
        #exiting
        sys.exit(1)
#setting vairbales for percentages
    percent_unvac_cases = 0
    percent_fully_vac_cases = 0

    #variable for reading of the opened file
    fileReader = csv.reader(file_fh)
    #opening file for writing
    with open('graphing_file.csv', 'w') as file:
        writer = csv.writer(file)
        # categories
        line1 = ["DATE", "% of ICU_CASES", "VACCINE_STATUS"]
        writer.writerow(line1)
        checker = False
        next(fileReader)
      #for row date in file reader
        for row_data_fields in fileReader:
          #formatting
            convertDate = datetime.date.fromisoformat(row_data_fields[0])
          #if convert date is = to startDate
            if convertDate == startDateConv:
              #thorugh calculations getting the rate of non and fully vaccinated cases
                percent_unvac_cases = (
                    (int(row_data_fields[1])) / Vac_cases) * 100
                percent_fully_vac_cases = (
                    (int(row_data_fields[3])) / Unvac_cases) * 100
                #row = [row_data_fields[0], percent_unvac_cases,percent_fully_vac_cases]
                row1 = [
                    row_data_fields[0], percent_unvac_cases,
                    "ICU_UNVACCINATED_CASES"
                ]
                row2 = [
                    row_data_fields[0], percent_fully_vac_cases,
                    "ICU_FULLY_VACCINATED_CASES"
                ]
                #writing rows for both 
                writer.writerow(row1)
                writer.writerow(row2)
              #printing for Unvac_cases
                print('{},{:.2e},{}'.format(row_data_fields[0],
                                            percent_unvac_cases,
                                            "ICU_UNVACCINATED_CASES"))
              #printing for Vac_cases
                print('{},{:.2e},{}'.format(row_data_fields[0],
                                            percent_fully_vac_cases,
                                            "ICU_FULLY_VACCINATED_CASES"))

                checker = True
          #if the checker is 
            if checker == True and convertDate != startDateConv:
              #calculating percentages for unvac cases
                percent_unvac_cases = (int(row_data_fields[1])) / Vac_cases
              #calculating percentages for full vac cases
                percent_fully_vac_cases = (int(
                    row_data_fields[3])) / Unvac_cases
              
                row1 = [
                    row_data_fields[0], percent_unvac_cases,
                    "ICU_UNVACCINATED_CASES"
                ]
                row2 = [
                    row_data_fields[0], percent_fully_vac_cases,
                    "ICU_FULLY_VACCINATED_CASES"
                ]
              #writing rows 
                writer.writerow(row1)
                writer.writerow(row2)
              #printing ICU_UNVACINATED_CASES
                print('{},{:.2e},{}'.format(row_data_fields[0],
                                            percent_unvac_cases,
                                            "ICU_UNVACCINATED_CASES"))
              #printing ICU_FULLY_VACINATED_CASES
                print('{},{:.2e},{}'.format(row_data_fields[0],
                                            percent_fully_vac_cases,
                                            "ICU_FULLY_VACCINATED_CASES"))
            #once it conv date reaches the last date then exit the program because were finished
            if convertDate == endDateConv:
                sys.exit(1)


#calling the main function
main(sys.argv)
