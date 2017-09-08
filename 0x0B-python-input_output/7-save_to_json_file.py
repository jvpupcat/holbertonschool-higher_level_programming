#!/usr/bin/python3
"""function that writes an obj to a text file, using a JSON rep"""


import json
def save_to_json_file(my_obj, filename):
    with open(filename, mode='w') as a_file:
        json.dump(my_obj, a_file)
