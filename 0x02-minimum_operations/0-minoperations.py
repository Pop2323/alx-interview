#!/usr/bin/python3

"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n: input value

    Returns:
        number of operations
    """

    if n < 2:
        return 0
    list_of_factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            while n % i == 0:
                n /= i
                list_of_factors.append(i)
        i += 1
    return sum(list_of_factors)

