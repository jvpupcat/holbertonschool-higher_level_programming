#!/usr/bin/python3
"""Module that prints text with newlines after .?:"""


def text_indentation(text):
    add_newline = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    if "." in text and "?" in text and ":" in text:
        add_newline = text.replace(". ", ".")
        add_newline = add_newline.replace(".", ".\n\n")
        add_newline = add_newline.replace("? ", "?\n\n")
        add_newline = add_newline.replace(": ", ":\n\n")
        print("{}".format(add_newline), end="")
