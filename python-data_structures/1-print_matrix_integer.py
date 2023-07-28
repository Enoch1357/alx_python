#! /usr/bin/python
def print_matrix_integer(matrix=""):
    for i in matrix:
        for k in i:
            print("{:d}".format(k), end=" ")
        print("", end="\n")
    return matrix
