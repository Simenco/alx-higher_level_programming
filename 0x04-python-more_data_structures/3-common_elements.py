#!usr/bin/python3

"""
this function returns a set of common elements in
the two sets
"""


def common_elements(set_1, set_2):
    for a in  set_1:
        for b in set_2:
            if a == b:
                return a
