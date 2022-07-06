#!/usr/bin/python3

"""
this function adds all uniqu integers
in a list (only once for each integers
"""


def uniq_add(my_list=[]):
    res = sum(set(my_list))
    return res
