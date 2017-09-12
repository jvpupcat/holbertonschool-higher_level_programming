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
