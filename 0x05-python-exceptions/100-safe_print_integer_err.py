#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    if type(value) is int:
        try:
            print("{:d}".format(value))
            return True
        except TypeError as te:
            print("Exception: {}".format(te), file=stderr)
            return False
        except ValueError as ve:
            print("Exception: {}".format(ve), file=stderr)
            return False
