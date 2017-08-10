#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        sort_list = sorted(my_list)
        length2 = len(sort_list)
        largest = my_list[0]
        for i in range(1, length2):
            if sort_list[i] > largest:
                largest = sort_list[i]
        return (largest)
