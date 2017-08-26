#!/usr/bin/python3
def print_square(size):
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        for x in range(0, size):
            for y in range(0, size):
                print("#", end="")
            print("")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
