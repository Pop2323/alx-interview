#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the game based on the given rules.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of integers where each integer
        represents the number of elements in the array for that round.
        
    Returns:
        str: The winner of the game ("Ben" or "Maria").
        Returns None if there is no winner or if input is invalid.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Determine the winner for each round
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """
    Mark the multiples of a given number `x`
    as non-prime in the list `ls`.
    
    Args:
        ls (list): List of integers representing primality
        (1 for prime, 0 for non-prime).
        x (int): The base number whose multiples will
        be marked as non-prime.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
