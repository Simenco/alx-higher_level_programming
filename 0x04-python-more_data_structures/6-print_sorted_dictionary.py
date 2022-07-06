#!/usr/bin/python3

"""
this function prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(key, a_dictionary[key])) for key in sorted(a_dictionary)]
