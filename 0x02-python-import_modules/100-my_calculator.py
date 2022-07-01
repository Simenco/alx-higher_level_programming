#!/usr/bin/python3

"""
This program imports all functions from the file calculator_1.py
and handles basic operations

"""
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)

    if n != 4:
        print("Usage: ./100-my_calculator.py a operator b")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
