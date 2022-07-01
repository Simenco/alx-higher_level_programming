#!/usr/bin/python3

"""
This program prints the number of and the list of
its arguments

"""
if __name__ == "__main__":
    import sys

    num_of_elements = len(sys.argv) - 1

    if num_of_elements == 0:
        print("0 arguments.")

    elif num_of_elements == 1:
        print("1 arguments.")

    else:
        print("{} arguments:".format(num of elements))

    for a in range(num_of_elements):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
