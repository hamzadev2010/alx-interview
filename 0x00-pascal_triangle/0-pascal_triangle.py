#!/usr/bin/python3
def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n)
    """
    triangle = []

    if n <= 0:
        return triangle

    i = 0
    while i < n:
        row = []
        j = 0
        while j <= i:
            if j == 0 or j == i:
                row.append(1)
            else:
                if i >= 2:
                    x = triangle[i - 1][j - 1]
                    y = triangle[i - 1][j]
                    row.append(x + y)
            j += 1
        triangle.append(row)
        i += 1

    return triangle
