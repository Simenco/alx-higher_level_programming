#!/usr/bin/python3

"""
This function element at specific position
in a given list without using pop() and importing
any module
"""


def delete_at(my_list=[], idx=0):
    ele = len(my_list)
    if (idx < 0) or (idx >= ele):
        return my_list
    del my_list[idx]
    return my_list
