#! /usr/bin/python
def print_matrix_integer(matrix=""):
    for i in matrix:
        without_last_member = i[:-1]
        for k in without_last_member:
            print("{:d}".format(k), end=" ")
        last_member = i[-1:]
        for j in last_member:
            print("{}".format(j))
        print(end="")
    return matrix
