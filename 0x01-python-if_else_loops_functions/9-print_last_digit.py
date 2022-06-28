#!/usr/bin/python3

# this function prints the last digit of a number

def print_last_digit(number):
    digit = number % 10
    if number < 0:
        return -digit
    return digit
