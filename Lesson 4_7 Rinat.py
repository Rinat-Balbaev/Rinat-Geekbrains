from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
user_number = abs(int(input('Enter a positive integer for factorial calculation: ')))
for i in gen:
    if x < user_number:
        print(i)
        x += 1
    else:
        break