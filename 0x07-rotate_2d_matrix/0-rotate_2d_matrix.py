#!/usr/bin/python3
'''an n x n 2D matrix, rotate it 90 degrees clockwise.'''

def rotate_2d_matrix(matrix):
    start, end = 0, len(matrix) - 1

    while start < end:
        for index in range(end - start):
            top_row, bottom_row = start, end
            top_left_value = matrix[top_row][start + index]
            matrix[top_row][start + index] = matrix[bottom_row - index][start]
            matrix[bottom_row - index][start] = matrix[bottom_row][end - index]
            matrix[bottom_row][end - index] = matrix[top_row + index][end]
            matrix[top_row + index][end] = top_left_value
        end -= 1
        start += 1
