import numpy as np
import random

# lista słów
word_list = np.array(['mouse', 'dog', 'cat', 'Angelka'])

# wypisanie słów obok siebie
for x in range(5):
    random.shuffle(word_list)
    print(*word_list, sep=" ")