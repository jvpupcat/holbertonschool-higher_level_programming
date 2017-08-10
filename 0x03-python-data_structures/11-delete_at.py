#!/usr/bin/python3
def is_valid(my_list, idx):
    length = len(my_list)
    if length == 0:
        return False
    elif length <= idx:
        return False
    elif idx < 0:
        return False
    return True


def delete_at(my_list=[], idx=0):
    if my_list:
        if is_valid(my_list, idx):
            del my_list[idx]
        return my_list
