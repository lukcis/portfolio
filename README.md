# README

## Overview
This repository contains four Python programs focusing on different functionalities:

**Complaint_form:** This program allows employees to submit complaints regarding company-related issues. It collects various details such as order number, employee name, customer name, company name, complaint item, reason, resolution, and additional information. The data is stored in a CSV file.

**Complaint_form_with_GUI:** Similar to the first program, this version provides a graphical user interface (GUI) built using Tkinter library. Employees can fill in complaint details in a user-friendly interface and submit them. Mandatory fields are validated, and the data is saved in a CSV file.

**Address_book:** This program serves as a basic address book where users can input personal details like name, last name, age, and street. Data input is validated, and the user is prompted to provide correct information if invalid data is entered. The collected data is stored in a CSV file and can be sorted based on user preference.

**Data_visualization:** This program visualizes various datasets using Matplotlib and Seaborn libraries. It includes three visualizations:
    - Total Investment by Continent and Year: A bar plot depicting the total investment by continent over different years.
    - Sum of Profit by Year: A bar plot showing the sum of profits over different years.
    - Imports and Exports by Continent: A bar plot illustrating the total imports and exports by continent.

## Usage
**Complaint Forms:**
    - Run either complaint_form.py for the text-based version or complaint_form_with_gui.py for the GUI version.
    - Fill in the required details in the form.
    - Submit the form, and the data will be saved in a CSV file.

**Address Book:**
    - Run address_book.py.
    - Follow the prompts to input personal details for each entry.
    - The data will be stored in a CSV file and can be sorted based on user preference.

**Data Visualization:**
    - Run data_visualization.py.
    - Three different visualizations will be displayed sequentially.

## Requirements
- Python 3.x
- Pandas
- Tkinter (for GUI)
- Matplotlib
- Seaborn

## Data Files
- **For the complaint forms**, the data is stored in complaint_data.csv.
- **For the address book**, the data is stored in address_book_data.csv.
- **For data visualization**, various datasets are used:
    - countries.csv
    - economies.csv
    - Coffee Chain.csv

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features.

## Author
Łukasz Ciskowski
