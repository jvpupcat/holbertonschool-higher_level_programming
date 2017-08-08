#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for a in range(0, len(my_list)):
        if my_list[a] == idx + 1:
            my_list[a] = element
    return (my_list)
