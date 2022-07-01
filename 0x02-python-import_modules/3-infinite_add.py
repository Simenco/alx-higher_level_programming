#!/usr/bin/python3

"""
This program prints the number of and the list of
its arguments

"""
if __name__ == "__main__":
    import sys

    total = 0
    n = len(sys.argv)

    for a in range(1, n):
        total += int(sys.argv[a])
    print("{}".format(total))
