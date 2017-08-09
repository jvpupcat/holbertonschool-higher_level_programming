#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    for a in range(0, len(copy_list)):
        if copy_list[a] == idx + 1:
            copy_list[a] = element
    return (copy_list)
