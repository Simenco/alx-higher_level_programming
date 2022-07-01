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
        print("Usage: ./100-my_calculator.py a operator b\n")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    operators = ["+", "-", "*", "/"]
        
    if operator not in operators:
        print("unknown operator, Available operators: +, -, * and /\n")
        sys.exit(1)

    if operator == "+":
        res = add(a, b)

    elif operator == "-":
        res = sub(a, b)

    elif operator == "*":
        res = mul(a, b)

    else:
        res = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, res))
