#!/usr/bin/python3
for a in range(0, 9):
    for b in range(0, 10):
        if a != b and b > a:
            print("{}{}".format(a, b), sep='', end='')
            if a != 8 or b != 9:
                print(", ", end='')
print('')
