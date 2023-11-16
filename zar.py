# write code that simulates 3 random numbers
import random

def random_numbers():
    for i in range(3):
        yield random.randint(1, 6)
        
for num in random_numbers():
    print(num)