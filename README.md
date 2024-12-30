# Covid19DataAnalysis

## Description

This is a Python program that compares the vaccination status and the rate of ICU cases in Ontario. It is capable of processing large CSV files. The user can graph the data to help better visualize it. 

## Getting Started
### Dependencies

* It requires no prerequisites, libraries and OS version. You would need a terminal, the files in this repository and Python installed on the device (if running on locally). 

### Executing program

* How to build and run the program
```
file: create_age_vac_status.py
python create_age_vac_status.py 2021 09 13 2022 03 19 cases_by_age_vac_status.csv 60-79

file: create_cases_mental_health.py
python create_cases_mental_health.py 18-24 65+ Mental_Health.csv 

file: create_icu_cases.py
python create_icu_cases.py 2021 08 11 2022 05 28 vac_status_hosp_icu.csv

file: create_vac_rate.py
python create_vac_rate.py 2021 08 11 2022 02 28 cases_by_vac_status.csv vac_status_hosp_icu.csv

file: graphing_create_vac_rate.py
python graphing_create_vac_rate.py graphing_file.csv IDs.pdf

file:  graphing_mental_health_cases.py
python graphing_mental_health_cases.py graphing_file.csv IDs.pdf

```

## Author Information
Your name: Shrina Patel<br />
Email: shrinapatel359@gmail.com
