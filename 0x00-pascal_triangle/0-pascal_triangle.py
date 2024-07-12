#!/usr/bin/python3
"""
0. This is Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
    n (int): The number of levels of the Pascal's triangle.

    Returns:
    list: A list of lists where each inner list
    represents a level in Pascal's triangle.
    """

    triangle = []
    if n > 0:
        for level in range(n):
            row = []
            coeff = 1

            for element in range(level + 1):
                row.append(coeff)
                coeff = coeff * (level - element) // (element + 1)

            triangle.append(row)
    return triangle
