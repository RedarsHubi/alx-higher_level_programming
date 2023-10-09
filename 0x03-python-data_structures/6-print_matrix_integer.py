#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if len(row) == 0:
            print()
        for element in row:
            if element == row[-1]:
                print("{:d}".format(element), end='')
            else:
                print("{:d}".format(element), end=' ')
        print()
