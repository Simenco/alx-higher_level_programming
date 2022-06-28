#!/usr/bin/python3

# this function computes a to the power of b
# and returns the value

def pow(a, b):
    res = a * pow(a, b - 1)
    return (res)
