#!/usr/bin/python3

"""
This function prints all integers of a list,
format: one integer per line withput importing any module
"""
def print_list_integer(my_list=[]):
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))