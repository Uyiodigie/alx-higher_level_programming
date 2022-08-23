#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
length = number[-1]
if length > 5:
    string = "and is greater than 5"
if length == 0:
    string = "and is 0"
if length < 6 and is not 0:
    string = "and is less than 6 and not 0"

print(f"Last digit of {number} is {length} {string}")
