#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    for c in range(0, len(new_string)):
        if new_string[c] == chr(67):
            new_string = new_string.strip('C')
        elif new_string[c] == chr(99):
            new_string = new_string.strip('c')
        else:
            return (new_string)
