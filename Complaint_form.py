# complaint form for company from employee side

import pandas as pd
from datetime import date
import os


file_path = 'E:\\Programowanie\\Projekty\\zapisane_rzeczy_z_projektów\\complaint_data.csv'

# Check if the file exists
if os.path.exists(file_path):
    complaint_DataFrame = pd.read_csv(file_path)
else:
    complaint_DataFrame = pd.DataFrame(columns=['OR', 'EMPLOYEE_NAME', 'CUSTOMER_NAME',
                                                'COMPANY', 'ITEM', 'REASON', 'RESOLUTION', 'INFO', 'DATE'])

print(complaint_DataFrame)


# Add input
input_or = str(input("Please provide your order number (OR-XXXXX):"))
while input_or == '':
    input_or = str(input("MENTADORY - Please provide your order number (OR-XXXXX):"))

input_your_name_last_name = str(input("Please provide your full name:"))
while input_your_name_last_name == '':
    input_your_name_last_name = str(input("MENTADORY - Please provide your full name:"))

input_customer_name_last_name = str(input("Please provide customer full name:"))
while input_customer_name_last_name == '':
    input_customer_name_last_name = str(input("MENTADORY - Please provide customer full name:"))

input_company = str(input("Please provide company name:"))
while input_company == '':
    input_company = str(input("MENTADORY - Please provide company name:"))

input_complaint_item = str(input("Please provide complain item name:"))
while input_complaint_item == '':
    input_complaint_item = str(input("MENTADORY - Please provide complain item name:"))

input_complaint_reason = str(input("Please provide the reason for the complaint:"))
while input_complaint_reason == '':
    input_complaint_reason = str(input("MENTADORY - Please provide the reason for the complaint:"))

input_complaint_resolution = str(input("Please provide expected resolution of the complaint:"))
while input_complaint_resolution == '':
    input_complaint_resolution = str(input("MENTADORY - Please provide expected resolution of the complaint:"))

input_additional_info = str(input("Please provide additional information if needed:"))
today_date = date.today()

# Append new data to the DataFrame
new_row = {'OR': input_or, 'EMPLOYEE_NAME': input_your_name_last_name, 'CUSTOMER_NAME': input_customer_name_last_name,
           'COMPANY': input_company, 'ITEM': input_complaint_item, 'REASON': input_complaint_reason,
           'RESOLUTION': input_complaint_resolution, 'INFO': input_additional_info, 'DATE': today_date}


# Add and save to csv
complaint_DataFrame = pd.concat([complaint_DataFrame, pd.DataFrame([new_row])], ignore_index=True)
complaint_DataFrame.to_csv(file_path, index=False)