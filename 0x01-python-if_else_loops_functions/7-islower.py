#!/usr/bin/python3
def islower(c):
    a = ord('a')
    z = ord('z')

    if ord(c) >= a and ord(c) <= z:
        return True
    else:
        return False
