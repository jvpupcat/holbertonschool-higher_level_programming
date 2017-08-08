#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    for a in my_list:
        if a == idx:
            my_list[a] = element
    return (my_list)
