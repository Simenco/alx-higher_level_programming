#!/usr/bin/python3

"""
This program prints the number of and the list of
its arguments

"""
if __name__ == "__main__":
    import sys

    total = 0
    num_of_elements = len(sys.argv) - 1

    for a in range(num_of_elements):
        total += sys.argv[a + 1]
        print("{}".format(total))
