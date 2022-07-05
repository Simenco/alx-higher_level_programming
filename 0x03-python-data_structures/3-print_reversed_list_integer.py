#!/usr/bin/python3

"""
this function prints alli integers of a list,
in reverse order, one integer per line
"""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list.pop()))
