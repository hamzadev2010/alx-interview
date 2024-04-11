def pascal_triangle(n):
    """
    rturns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for row_num in range(n):
        row = []
        for col_num in range(row_num + 1):
            if col_num == 0 or col_num == row_num:
                row.append(1)
            else:
                prev_row = triangle[row_num - 1]
                value = prev_row[col_num - 1] + prev_row[col_num]
                row.append(value)
        triangle.append(row)

    return triangle
