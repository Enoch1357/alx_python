#! /usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [[(x**2) for x in i] for i in matrix]
    return squared_matrix