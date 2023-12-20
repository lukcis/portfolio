import numpy as np

# komputer losuje liczbe
#np.random.seed(42)
random_number = np.random.randint(10)
#print(random_number)
num = 20

# człowiek zgaduje liczbe
# komputer porównuje wartości
while random_number != num:
    num = int(input("Enter an integer number in range 0 to 10: "))
else:
    print('Nice! You got it!')