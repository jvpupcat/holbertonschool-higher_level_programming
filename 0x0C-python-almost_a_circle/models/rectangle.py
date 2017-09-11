#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base
class Rectangle(Base):
    """initialize rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def display(self):
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def update(self, *args, **kwargs):
        if len(args) == 5:    
            self.y = args[4]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if 'id' in kwargs:
            self.id = kwargs['y']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'y' in kwargs:
            self.y = kwargs['y']
        if 'x' in kwargs:
            self.x = kwargs['x']
        return (self)
