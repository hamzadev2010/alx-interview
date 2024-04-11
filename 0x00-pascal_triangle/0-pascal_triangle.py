#!/usr/bin/python3
"""Triangle of pascale """


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n)
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            prev_row = pascal_triangle[i - 1]
            new_value = prev_row[j - 1] + prev_row[j]
            row.append(new_value)

        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
