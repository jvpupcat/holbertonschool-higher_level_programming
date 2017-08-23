#!/usr/bin/python3
"""This class contains documentation for class Square"""
"""__init__ method & instantiation of size after class Square:"""
"""if/else stmnt to make sure size is an int"""
"""def area(self): multiplies self to self"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print("")
