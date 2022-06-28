#!/usr/bin/python3

# this function prints a string in uppercase

def uppercase(str):
    for c in str:
        char = ord(c)
        if (char in range(97, 123)):
            c = chr(char - 32)
        print("{}".format(c), end="")
    print(" ")
