#!/usr/bin/python3

"""
this program prints all the names defined by
module hidden_4.pyc

"""
if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print(i)
