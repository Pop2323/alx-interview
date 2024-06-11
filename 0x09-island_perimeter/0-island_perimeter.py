#!/usr/bin/python3
"""function  that returns the perimeter of
    the island described in grid"""


def island_perimeter(grid):
    """grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    land_cell = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                land_cell += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return land_cell * 4 - edges * 2
