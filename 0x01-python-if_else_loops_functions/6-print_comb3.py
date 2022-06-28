#!/usr/bin/python3

# this program all possible different
# combination of two digits. e.g 01 and 10
# are same. The two digits must be different

for n in range(0, 10):
    for m in range(n + 1, 10):
        if n == 8 and m == 9:
            print("{}{}".format(n, m))
        else:
            print("{}{}".format(n, m), end=", ")
