#!/usr/bin/python3

"""
This program prints the number of and the list of
its arguments

"""
if __name__ == "__main__":
    import sys

    n = len(sys.argv)

    if n == 1:
        print("0 arguments.")

    elif n == 2:
        print("1 arguments:")

    else:
        print("{} arguments:".format(n - 1))

    for a in range(1, n):
        print("{}: {}".format(a, sys.argv[a]))
