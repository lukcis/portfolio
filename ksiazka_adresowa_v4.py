import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path
import json
import re
import string
import math
import csv


# stworzenie pustej dictionary
adress_book = {}
adress_book = pd.read_csv('E:\\Programowanie\\Projekty\\zapisane_rzeczy_z_projektów\\name_of_file.csv')
adress_book_df = pd.DataFrame.from_dict(adress_book, orient='index')
adress_book_df_Trans = adress_book_df.T
print(adress_book_df_Trans)
# wprowadzenie danych przez użytkownika
adress_book_df_Trans['name'] = str(input("Podaj imię: "))
name_str = adress_book_df_Trans['name']

# sprawdzenie czy podane imię jest ciągiem znaków od A do Z
def isvalidname(input):
    return input.replace(" ","").isalpha()

while isvalidname(name_str) is False:
    adress_book_df_Trans['name'] = str(input("Imię nie może posiadać liczb: "))
    name_str = adress_book_df_Trans['name']

# wprowadzenie danych przez użytkownika
adress_book_df_Trans['last_name'] = str(input("Podaj nazwisko: "))
last_name_str = adress_book_df_Trans['last_name']

#sprawdzenie czy podane nazwisko jest ciągiem znaków od A do Z
def isvalidname(input1):
    return input1.replace(" ","").isalpha()

while isvalidname(last_name_str) is False:
    adress_book_df_Trans['last_name'] = str(input("Nazwisko nie może posiadać liczb: "))
    last_name_str = adress_book_df_Trans['last_name']

# wprowadzenie danych przez użytkownika
age_str = input("Podaj wiek: ")
def IsValidName_1(input2):
    return input2.replace(" ","").isalpha()
while IsValidName_1(age_str) is True:
    age_str = input("Podaj wiek, jako liczbę: ")
else:
    age_int = int(age_str)

adress_book_df_Trans['age'] = age_int

# wprowadzenie danych przez użytkownika
adress_book_df_Trans['street'] = str(input("Podaj ulicę zamieszkania: "))
street_str = adress_book_df_Trans['street']

#sprawdzenie czy podana ulica jest ciągiem znaków od A do Z
def IsValidName(input1):
    return input1.replace(" ","").isalpha()

while IsValidName(street_str) is False:
    adress_book_df_Trans['last_name'] = str(input("Podaj samą ulicę, bez numeru domu/mieszkania: "))
    street_str = adress_book_df_Trans['last_name']

# sortowanie wprowadzonych danych

# column_name = list(adress_book.keys())
# print(column_name)
# sorted_question = str(input("Podaj zmienną po której chcesz posortować dane: " + str(column_name) + ": "))
#
# if sorted_question == 'name':
#     adress_book.sort_values(by=['name'])
# if sorted_question == 'last_name':
#     print("l")
# if sorted_question == 'age':
#     print("a")
# if sorted_question == 'street':
#     print("s")


# zapisanie książki adresowej do pliku txt

save_path = 'E:\\Programowanie\\Projekty\\zapisane_rzeczy_z_projektów'
#name_of_file = str(input("What is the name of the file: "))
completeName = os.path.join(save_path, 'name_of_file' +".csv")
file = open(completeName, "w")
json.dump(adress_book, file)
file.close()
file = open(completeName, "r")
output = file.read()
print(output)
file.close()
