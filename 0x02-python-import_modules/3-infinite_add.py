#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0

    if len(sys.argv) == 1:
        print("0")
    for i in range(1, len(sys.argv)):
        total = total + int(sys.argv[i])
    print("{:d}".format(total))
