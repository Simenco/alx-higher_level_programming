#!/usr/bin/python3

"""
This program imports a module that adds two
integer numbers together and produces result

"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
