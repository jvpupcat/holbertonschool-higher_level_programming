#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""
"""and returns the number of characters added"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
