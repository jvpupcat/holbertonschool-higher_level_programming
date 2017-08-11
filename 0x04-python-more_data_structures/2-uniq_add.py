#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique = set(my_list)
    for i in unique:
        total = total + i
    return (total)
