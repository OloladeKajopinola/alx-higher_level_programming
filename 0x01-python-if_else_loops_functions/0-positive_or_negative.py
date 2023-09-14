#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-100, 100)

# Check if the number is positive, zero, or negative
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
