#!/usr/bin/python3
for alphabet in range(97, 123):
    alphabet = chr(alphabet)
    if alphabet not in "qe":
        print(f"{alphabet}", end="")
