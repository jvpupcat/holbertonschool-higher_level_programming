#!/usr/bin/python3
for z in range(122, 96, -1):
        print("{:s}".format(chr(z - 32) if z % 2 == 1 else chr(z)), end='')
