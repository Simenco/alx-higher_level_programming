#!/usr/bin/python3

"""
this function replaces all occurrences of an element
by another in a new list
@my_list: the initial list
@search: is the element to replace
@replace: is the new element
"""


def search_replace(my_list, search, replace):
    new_list = [ele if ele != search else replace for ele in my_list]
    return new_list
