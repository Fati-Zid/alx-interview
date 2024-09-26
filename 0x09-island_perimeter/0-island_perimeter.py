#!/usr/bin/python3
"""
   Calculate the perimeter of the island described in the grid.

    Parameters:
    grid (List[List[int]]): A 2D list representing the map where 0 indicates water and 1 indicates land.

    Returns:
    int: The perimeter of the island.
"""
def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the top cell
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check the bottom cell
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check the left cell
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check the right cell
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter