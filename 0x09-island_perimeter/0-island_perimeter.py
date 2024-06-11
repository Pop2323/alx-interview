def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    num_land_cells = 0
    num_shared_edges = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                num_land_cells += 1

                if col > 0 and grid[row][col - 1] == 1:
                    num_shared_edges += 1

                if row > 0 and grid[row - 1][col] == 1:
                    num_shared_edges += 1

    perimeter = num_land_cells * 4 - num_shared_edges * 2
    return perimeter
