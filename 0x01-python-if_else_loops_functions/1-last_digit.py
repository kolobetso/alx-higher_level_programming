#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    reminder = (number % -10)
else:
    reminder = (number % 10)

print(f"Last digit of {number:d} is {reminder:d} and is ", end="")
if reminder > 5:
     print("greater than 5")
elif reminder == 0:
     print("0")
else:
     print("less than 6 and not 0")
