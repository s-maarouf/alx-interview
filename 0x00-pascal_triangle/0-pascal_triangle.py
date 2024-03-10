#!/usr/bin/python3

"""A function that takes n as input number and returns Pascal's triangle"""


def pascal_triangle(n: int):
    """Pascal's triangle"""
    triangle = [[1]]
    if type(n) is not int or n <= 0:
        triangle = []
        return triangle
    else:
        for i in range(n - 1):
            row = [1]
            for j in range(i):
                row.append(triangle[-1][j] + triangle[-1][j+1])
            row.append(1)
            triangle.append(row)
        return triangle
