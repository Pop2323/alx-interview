#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List[List[int]] - A list of lists of
    integers where 0 represents water and 1 represents land.
    :return: int - The perimeter of the island.
    """
    height = len(grid)
    width = len(grid[0])
    num_land_cells = 0
    num_shared_edges = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                num_land_cells += 1

                # Check for shared edges with the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    num_shared_edges += 1

                # Check for shared edges with the top cell
                if i > 0 and grid[i - 1][j] == 1:
                    num_shared_edges += 1

    # Each land cell contributes 4 to the perimeter,
    # each shared edge subtracts 2
    perimeter = num_land_cells * 4 - num_shared_edges * 2
    return perimeter
