#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        print("{:d}".format(a/b)
    except (ArithmeticError, TypeError):
        None
    finally:
        print("{}".format(a//b))
