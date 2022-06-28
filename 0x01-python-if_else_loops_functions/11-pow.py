#!/usr/bin/python3

# this function computes a to the power of b
# and returns the value

def pow(a, b):
    if b == 0:
        return a
    res = a * pow(a, b - 1)
    return (res)
