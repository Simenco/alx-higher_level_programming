#!/usr/bin/python3

# this program prints the ASCII alphabet in reverse
# alternating lowercase and uppercase
# i.e z in lowercase and Y in uppercase

for c in range(90, 64, -1):
    if (c % 2 == 0):
        ch = chr(c + 32)
    else:
        ch = chr(c)
    print("{}".format(ch), end="")
