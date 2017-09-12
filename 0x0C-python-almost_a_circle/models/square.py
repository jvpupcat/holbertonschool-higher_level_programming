#!/usr/bin/python3
"""class square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
        if 'size' in kwargs:
            self.width = kwargs['size']
