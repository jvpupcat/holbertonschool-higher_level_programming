#!/usr/bin/python3
"""a function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as a_file:
        lines_of_x = 0
        for x in a_file:
            lines_of_x += 1
        return (lines_of_x)
