#!/usr/bin/python3

"""
this function deletes a key in a
dictionary ...
if a key does not, dictionary wont change
"""


def simple_delete(a_dictionary, key=""):
    if key in  a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
