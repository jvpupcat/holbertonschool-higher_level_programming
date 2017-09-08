#!/usr/bin/python3
"""a function that writes a string to a text file and returns the"""
"""number of characters written"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
