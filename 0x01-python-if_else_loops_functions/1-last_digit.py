#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of"
b = "and is greater than 5"
c = "and is less than 6 and not 0"
if number < 0:
    mod = -number % 10 * -1
else:
    mod = number % 10
if mod >= 6:
    print("{} {:d} is {:d} {}".format(a, number, mod, b))
elif mod == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, mod))
else:
    print("{} {:d} is {:d} {}".format(a, number, mod, c))
