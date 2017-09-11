#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
