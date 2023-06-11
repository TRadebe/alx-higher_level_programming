#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import sub, add, div, mul
    import sys

    signs = {'+': add, '-': sub, '/': div, '*': mul}
    if len(sys.argv) -1 != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif sys.argv[2] not in signs.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    elif sys.argv[2] in signs:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, signs[sys.argv[2]](a, b)))
