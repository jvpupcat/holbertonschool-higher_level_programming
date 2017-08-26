#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) is str and type(last_name) is str:
        print("My name is {:s} {:s}".format(first_name, last_name))
    elif type(first_name) is not str:
        raise TypeError("first_name must be a string")
    else:
        raise TypeError("last_name must be a string")
