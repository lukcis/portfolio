import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path
import json
import re
import string
import math


# stworzenie pustej dictionary
adress_book = {}

# wprowadzenie danych przez użytkownika
adress_book['name'] = str(input("Podaj imię: "))
name_str = adress_book['name']

# sprawdzenie czy podane imię jest ciągiem znaków od A do Z
def isvalidname(input):
    return input.replace(" ","").isalpha()

while isvalidname(name_str) is False:
    adress_book['name'] = str(input("Imię nie może posiadać liczb: "))
    name_str = adress_book['name']

# wprowadzenie danych przez użytkownika
adress_book['last_name'] = str(input("Podaj nazwisko: "))
last_name_str = adress_book['last_name']

#sprawdzenie czy podane nazwisko jest ciągiem znaków od A do Z
def isvalidname(input1):
    return input1.replace(" ","").isalpha()

while isvalidname(last_name_str) is False:
    adress_book['last_name'] = str(input("Nazwisko nie może posiadać liczb: "))
    last_name_str = adress_book['last_name']

# wprowadzenie danych przez użytkownika
age_str = input("Podaj wiek: ")
def IsValidName_1(input2):
    return input2.replace(" ","").isalpha()
while IsValidName_1(age_str) is True:
    age_str = input("Podaj wiek, jako liczbę: ")
else:
    age_int = int(age_str)

adress_book['age'] = age_int

# wprowadzenie danych przez użytkownika
adress_book['street'] = str(input("Podaj ulicę zamieszkania: "))
street_str = adress_book['street']

#sprawdzenie czy podana ulica jest ciągiem znaków od A do Z
def IsValidName(input1):
    return input1.replace(" ","").isalpha()

while IsValidName(street_str) is False:
    adress_book['last_name'] = str(input("Podaj samą ulicę, bez numeru domu/mieszkania: "))
    street_str = adress_book['last_name']

# zapisanie książki adresowej do pliku txt
save_path = 'E:\Programowanie\Projekty\zapisane rzeczy z projektów'
name_of_file = str(input("What is the name of the file: "))
completeName = os.path.join(save_path, name_of_file+".txt")
file = open(completeName, "w")
json.dump(adress_book, file)
file.close()
file = open(completeName, "r")
output = file.read()
print(output)
file.close()
