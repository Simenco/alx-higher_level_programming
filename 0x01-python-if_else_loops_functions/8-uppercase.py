#!/usr/bin/python3

# this function prints a string in uppercase

def uppercase(str):
    for c in str:
        char = ord(c)
        if (char in range(97, 123)):
            up = chr(char - 32)
        else:
            up = chr(char)
        print("{}".format(up), end="")
    print(end=" \n")
