#!/usr/bin/python3

"""
this function computes the square of value of all integers
of a matrix
"""


def square_matrix_simple(matrix=[]):
    sq_r = [list(map(lambda x:x*x, ele)) for ele in matrix]
    return sq_r
