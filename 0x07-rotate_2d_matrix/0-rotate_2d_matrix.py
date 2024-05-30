#!/usr/bin/python3
"""Module for 2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    The function performs the rotation in two main steps:
    1. Reverse the order of the rows in the matrix.
    2. Swap the elements on the diagonals to transpose the matrix.

    Parameters:
    matrix (list of list of int): A 2D list representing the matrix to rotate.

    Example:
    Given the following matrix:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    After rotation, it becomes:
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    """
    
    # Step 1: Reverse the rows of the matrix
    matrix.reverse()
    
    # Step 2: Swap the elements on the diagonal to transpose the matrix
    for i in range(len(matrix)):
        for j in range(i):
            # Swap element at (i, j) with element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]