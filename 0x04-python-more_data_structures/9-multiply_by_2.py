#!/usr/bin/python3

"""
this function returns a dictionary with 
all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    return ({k, v*v for k, v in a_dictionary.items()})
