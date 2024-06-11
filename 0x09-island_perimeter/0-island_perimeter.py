#!/usr/bin/python3

def island_perimeter(grid):
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize variables to count land cells and shared edges
    num_land_cells = 0
    num_shared_edges = 0

    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is a land cell
            if grid[row][col] == 1:
                num_land_cells += 1

                # Check for a shared edge with the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    num_shared_edges += 1

                # Check for a shared edge with the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    num_shared_edges += 1

    # Calculate the perimeter using the number of land cells and shared edges
    perimeter = num_land_cells * 4 - num_shared_edges * 2
    return perimeter
