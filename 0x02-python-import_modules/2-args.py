#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    if len(sys.argv) == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
