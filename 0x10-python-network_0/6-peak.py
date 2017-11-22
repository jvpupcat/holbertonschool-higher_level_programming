#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    cursor = 0
    if list_of_integers is None:
        return
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    for cursor in range(0, len(list_of_integers)):
        for i in range(0, len(list_of_integers)):
            if list_of_integers[i] < list_of_integers[cursor]:
                store_max = list_of_integers[cursor]
            else:
                store_max = list_of_integers[cursor]
    return store_max
