#!/usr/bin/python3

"""
This function retrieves an element from a list,
"""


def element_at(my_list, idx):
    if idx < 0:
        return None
    ele = len(my_list)

    if idx >= ele:
        return None

    for a in range(ele):
        if idx == a:
            return (my_list[idx])
