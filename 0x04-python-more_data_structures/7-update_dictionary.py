#!/usr/bin/python3

"""
this function replaces or adds key/value in a
dictionary ...
if a key exists in the dictionary, value will be replaced
if a key does not, it will be created
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)
