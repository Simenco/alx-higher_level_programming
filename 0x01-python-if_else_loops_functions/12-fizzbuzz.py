#!/usr/bin/python3

# this function prints number from 1 - 100
# separated by space
# prints Fizz (multiple of 3), Buzz (multipls of 5)
# prints FizzBuzz (multiple of 3 and 5)

def fizzbuzz():
    for n in range(1, 101):
        if (n % 15 == 0):
            print("FizzBuzz", end=" ")
        elif (n % 3 == 0):
            print("Fizz", end=" ")
        elif (n % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{}".format(n), end=" ")
