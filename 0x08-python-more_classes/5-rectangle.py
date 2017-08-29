#!/usr/bin/python3
""" module that defines a rectangle - area and perimeter """
""" added eval() """


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        return (2 * (int(self.__width) + int(self.__height)))

    def __str__(self):
        emp_string = ""
        ret_string = (('#' * self.__width + '\n') * self.__height)
        if self.__width == 0 or self.height == 0:
            return emp_string
        return (ret_string[:-1])

    def __repr__(self):
        w = str(self.__width)
        h = str(self.__height)
        my_string = "Rectangle(" + w + ", " + h + ")"
        return my_string

    def __del__(self):
        print("Bye rectangle...")
        return
