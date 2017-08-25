#!/usr/bin/python3
def add_integer(a, b):
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is int and type(b) is int:
        return (a + b)
    elif type(a) is not int:
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
