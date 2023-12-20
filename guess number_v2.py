import numpy as np
import matplotlib.pyplot as plt

# komputer losuje liczbe
#np.random.seed(42)
random_number = np.random.randint(10)
#print(random_number)
num = 20

#komputer porównuje wartość wylosowanego numeru z podanym przez człowieka.
while random_number != num:
    try: # jeśli wartość nie jest liczbą całkowitą, zwraca informację z ValueError
        num = int(input("Enter an integer number in range 0 to 10: "))
    except ValueError:
        print('You can provide only integer')
else:
    print('Nice! You got it!')