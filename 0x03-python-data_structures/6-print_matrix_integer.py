#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i == len(matrix) - 1:
            print("{:d}".format(matrix[i]), end=',\n')
        else:
            print("{:d}".format(matrix[i]))
