#!/usr/bin/python3

import random

# Generate a random signed number
number = random.randint(-100, 100)

# Check if the number is positive, zero, or negative
if number > 0:
    result = "is positive"
elif number == 0:
    result = "is zero"
else:
    result = "is negative"

#Print the number and its status
print("The number {} {}".format(number, result))
