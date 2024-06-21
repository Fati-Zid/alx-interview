#!/usr/bin/python3
"""
  Returns a list of lists of integers representing the Pascal’s triangle of n :
  - Returns an empty list if n <= 0.
  - Assume that n will be always an integer.
  - hint: 
      -- Each element in the middle is the sum of the two elements above it.
"""

def pascal_triangle(n):
  """  Return an empty list if n <= 0 """
  if(n<= 0):
    return []
  """ start the first row by 1"""
  pascal_triangle = [[1]]

  """ Build other rows: using row i and column j """
  for i in range(1, n):
    row = [1] # <= first row
    for j in range(1, i):
      """ Calculate the midle element"""
      row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
    row.append(1) # <= end of the row
    pascal_triangle.append(row)
  
  return pascal_triangle