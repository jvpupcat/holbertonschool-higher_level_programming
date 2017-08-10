#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    return [[y**2 for y in x] for x in new_matrix]
