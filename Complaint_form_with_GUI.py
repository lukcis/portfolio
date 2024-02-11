# complaint form for company from employee side with GUI

import pandas as pd
from datetime import date
import os
import tkinter as tk
from tkinter import messagebox


def save_complaint():
    input_or = entry_or.get()
    input_your_name_last_name = entry_your_name_last_name.get()
    input_customer_name_last_name = entry_customer_name_last_name.get()
    input_company = entry_company.get()
    input_complaint_item = entry_complaint_item.get()
    input_complaint_reason = entry_complaint_reason.get()
    input_complaint_resolution = entry_complaint_resolution.get()
    input_additional_info = entry_additional_info.get()
    today_date = date.today()

    # Check for mandatory fields
    if not (input_or and input_your_name_last_name and input_customer_name_last_name and input_company):
        messagebox.showerror("Error", "Please fill in all mandatory fields.")
        return

    # Check if the file exists
    file_path = 'E:\\Programowanie\\Projekty\\data\\complaint_data.csv'
    if os.path.exists(file_path):
        complaint_dataframe = pd.read_csv(file_path)
    else:
        complaint_dataframe = pd.DataFrame(
            columns=['OR', 'EMPLOYEE_NAME', 'CUSTOMER_NAME', 'COMPANY', 'ITEM', 'REASON', 'RESOLUTION', 'INFO', 'DATE'])

    # Create a new row
    new_row = {'OR': input_or, 'EMPLOYEE_NAME': input_your_name_last_name,
               'CUSTOMER_NAME': input_customer_name_last_name, 'COMPANY': input_company,
               'ITEM': input_complaint_item, 'REASON': input_complaint_reason,
               'RESOLUTION': input_complaint_resolution, 'INFO': input_additional_info,
               'DATE': today_date}

    # Append the new row to the DataFrame
    complaint_dataframe = pd.concat([complaint_dataframe, pd.DataFrame([new_row])], ignore_index=True)

    # Drop duplicate rows
    complaint_dataframe = complaint_dataframe.drop_duplicates()

    # Save the DataFrame to the CSV file
    complaint_dataframe.to_csv(file_path, index=False)
    messagebox.showinfo("Success", "Complaint saved successfully.")


def clear_fields():
    # Clear all entry fields
    entry_or.delete(0, tk.END)
    entry_your_name_last_name.delete(0, tk.END)
    entry_customer_name_last_name.delete(0, tk.END)
    entry_company.delete(0, tk.END)
    entry_complaint_item.delete(0, tk.END)
    entry_complaint_reason.delete(0, tk.END)
    entry_complaint_resolution.delete(0, tk.END)
    entry_additional_info.delete(0, tk.END)


# Create GUI
root = tk.Tk()
root.title("Complaint Form")
root.geometry("1000x1000")

# Labels
tk.Label(root, text="Order Number - (OR-XXXXX)*:").grid(row=0, column=0)
tk.Label(root, text="Your Name:*").grid(row=1, column=0)
tk.Label(root, text="Customer Name:*").grid(row=2, column=0)
tk.Label(root, text="Company Name:*").grid(row=3, column=0)
tk.Label(root, text="Complaint Item:").grid(row=4, column=0)
tk.Label(root, text="Complaint Reason:").grid(row=5, column=0)
tk.Label(root, text="Complaint Resolution:").grid(row=6, column=0)
tk.Label(root, text="Additional Info:").grid(row=7, column=0)
tk.Label(root, text="* is mendatory").grid(row=8, column=0)


# Entry fields
entry_or = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_or.grid(row=0, column=1)
entry_your_name_last_name = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_your_name_last_name.grid(row=1, column=1)
entry_customer_name_last_name = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_customer_name_last_name.grid(row=2, column=1)
entry_company = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_company.grid(row=3, column=1)
entry_complaint_item = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_complaint_item.grid(row=4, column=1)
entry_complaint_reason = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_complaint_reason.grid(row=5, column=1)
entry_complaint_resolution = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_complaint_resolution.grid(row=6, column=1)
entry_additional_info = tk.Entry(root, width=30, font=("Times new roman", 14))
entry_additional_info.grid(row=7, column=1)


# Save button
save_button = tk.Button(root, text="Save", command=save_complaint, width=6, font=("Times new roman", 14))
save_button.grid(row=9, column=0, columnspan=2)
clear_button = tk.Button(root, text="Clear", command=clear_fields,  width=6, font=("Times new roman", 14))
clear_button.grid(row=9, column=1, columnspan=2)

root.mainloop()