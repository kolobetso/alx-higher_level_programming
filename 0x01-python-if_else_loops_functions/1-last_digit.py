#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    reminder = (number % -10)
else:
    reminder = (number % 10)

if reminder > 5:
    print(f"Last digit of {number:d} is {reminder} and is greater than 5")
elif reminder == 0:
    print(f"Last digit of {number:d} is {reminder:d} and is 0")
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, reminder))
