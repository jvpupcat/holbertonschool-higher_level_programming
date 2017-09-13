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
        super().__init__(id)

    @property
    def width(self):
        """getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """raise TypeError if not int and ValueError is <= 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """raise TypeError if not int and ValueError if <= 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter and setter for x"""
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
        """getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return int(self.__width) * int(self.__height)

    def display(self):
        """displays the hash table"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        """returns a string"""
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def update(self, *args, **kwargs):
        """returns key and value"""
        if len(args):
            for i, args in enumerate(args):
                if i == 4:
                    self.y = args
                elif i == 3:
                    self.x = args
                elif i == 2:
                    self.height = args
                elif i == 1:
                    self.width = args
                elif i == 0:
                    self.id = args
        else:
            if 'id' in kwargs:
                    self.id = kwargs['id']
            if 'height' in kwargs:
                    self.height = kwargs['height']
            if 'width' in kwargs:
                    self.width = kwargs['width']
            if 'y' in kwargs:
                    self.y = kwargs['y']
            if 'x' in kwargs:
                    self.x = kwargs['x']
            return (self)

    def to_dictionary(self):
        """create dictionary"""
        my_dict = {'id': self.id, 'width': self.width,
                   'x': self.x, 'y': self.y, 'height': self.height}
        return my_dict
