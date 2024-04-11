#!/usr/bin/env python3

def pascal_triangle(n):
    """
    rturns a list of lists of integers representing the Pascal’s triangle of n
    """
      triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)
        if i >= 2:
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
