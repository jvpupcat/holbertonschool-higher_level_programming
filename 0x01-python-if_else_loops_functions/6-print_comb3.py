#!/usr/bin/python3
for a in range(0, 9):
    for b in range(0, 10):
        if a != b and b > a and a != 8 and b != 9:
            print("{}{}, ".format(a, b), end='')
        if a == 8 and b == 9:
            print("{}{}".format(a, b), end='\n')
