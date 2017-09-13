#!/usr/bin/python3
"""class square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """initialized square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns string"""
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        """returns key and value"""
        if len(args):
            for i, args in enumerate(args):
                if i == 0:
                    self.id = args
                if i == 1:
                    self.size = args
                if i == 2:
                    self.x = args
                if i == 3:
                    self.y = args
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'size' in kwargs:
                self.size = kwargs['size']

    def to_dictionary(self):
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
