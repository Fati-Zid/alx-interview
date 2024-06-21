#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0.
- Assume that n will be always an integer.
- Hint:
  -- Each element in the middle is the sum of the two elements above it.
"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    pascal_triangle = [[1]]  # Start the first row with 1

    for i in range(1, n):
        row = [1]  # First element of the row is always 1
        for j in range(1, i):
            row.append(pascal_triangle[i - 1][j - 1]+pascal_triangle[i - 1][j])
        row.append(1)  # Last element of the row is always 1
        pascal_triangle.append(row)

    return pascal_triangle
