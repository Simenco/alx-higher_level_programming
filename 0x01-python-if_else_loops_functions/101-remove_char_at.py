#!/usr/bin/python3

# this function creates a copy of the string
# removes the character a position n

def remove_char_at(str, n):
    count = 0
    for i in str:
        count = count + 1
    if n < 0 or n > count:
        return str
    else:
        str = str[:n] + str[n+1:]
        return str
