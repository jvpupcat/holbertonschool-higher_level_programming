#!/usr/bin/python3
"""first class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to JSON string"""
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        js = []
        if list_objs:
            for obj in list_objs:
                js.append(obj.to_dictionary())
        js1 = cls.to_json_string(js)
        with open("{}.json".format(cls.__name__), 'w') as jsfile:
            jsfile.write(js1)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
