#!/usr/bin/python3
"""first class Base"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """assign the public instance attribute id"""
            self.id = id
        else:
            """increment and assign value to public instance attribute id"""
            Base.__nb_objects += 1
            self.id = self.__nb_objects
