# Adress book

import pandas as pd


adress_book_df = pd.DataFrame()

for x in range(3):

    adress_book = pd.DataFrame(index=[0])

# Input Name
    input_name = str(input("Please provide your name: "))

    def isvalid_name(input0):
        return input0.replace(" ", "").isalpha()

    while isvalid_name(input_name) is False:
        input_name = str(input("Name cannot contain numbers: "))


# Input Last Name
    input_last_name = str(input("Please provide your last name: "))

    def isvalid_last_name(input1):
        return input1.replace(" ", "").isalpha()

    while isvalid_last_name(input_last_name) is False:
        input_last_name = str(input("Last name cannot contain numbers: "))

    # Input Age
    def is_valid_age(input_str):
        try:
            int(input_str)
            return True
        except ValueError:
            return False

    age_str = input("Please provide your age: ")

    while not is_valid_age(age_str):
        age_str = input("Provide age as a number: ")

    age_int = int(age_str)

# Input Street
    input_street = str(input("Please provide your street: "))

    def isvalid_street(input3):
        return input3.replace(" ", "").isalpha()

    while isvalid_street(input_street) is False:
        input_street = str(input("Enter only the street, without house/apartment number:"))

    new_row = {'name': input_name, 'last_name': input_last_name, 'age': age_int, 'street': input_street}
    adress_book_df = pd.concat([adress_book_df, pd.DataFrame([new_row])], ignore_index=True)


print(adress_book_df)

# Sort data
column_names = list(adress_book_df.columns)
sorted_question = False

while sorted_question != 'True':
    if sorted_question in column_names:
        sorted_adress_book_df = adress_book_df.sort_values(by=sorted_question, ascending=True)
        break
    else:
        sorted_question = input("Please provide the variable by which you want to sort the data: "
                                + str(column_names) + ": ")


# Save to csv
save_path = 'E:\\Programowanie\\Projekty\\zapisane_rzeczy_z_projektów\\adress_book_data.csv'
adress_book_df.to_csv(save_path, index=False)