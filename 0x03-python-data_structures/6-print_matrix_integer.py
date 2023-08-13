#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for now in matrix:
        for i in range(len(row)):
            print('{:d}'.format(row[i]), end=(' ' * (i < len(row) - 1)))
        print('')
