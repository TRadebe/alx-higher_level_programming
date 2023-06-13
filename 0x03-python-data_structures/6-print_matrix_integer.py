#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for v in i:
            print('{:d}'.format(v), end='' if v == i[-1] else ' ')
        print()
