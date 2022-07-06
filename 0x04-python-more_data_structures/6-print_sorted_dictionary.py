#!/usr/bin/python3

"""
this function prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
