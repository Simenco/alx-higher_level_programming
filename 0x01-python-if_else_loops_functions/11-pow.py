#!/usr/bin/python3

# this function computes a to the power of b
# and returns the value

def pow(a, b):
    if b < 0:
        b = abs(b)
        res = pow(a, b)
        return (1 / res)
    if b == 0:
        return 1
    res = a * pow(a, b - 1)
    return (res)
