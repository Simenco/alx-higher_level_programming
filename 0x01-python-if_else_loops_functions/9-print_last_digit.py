#!/usr/bin/python3

# this function prints the last digit of a number

def print_last_digit(number):
    digit = abs(number) % 10
    if (number < 0):
        print("{}".format(-digit), end="")
        return -digit
    print("{}".format(digit), end="")
    return digit
