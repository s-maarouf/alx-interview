#!/usr/bin/python3

def pascal_triangle(n: int):
    if n <= 0:
        return [{}]
    else:
        triangle = [[1]]
        for i in range(n - 1):
            row = [1]
            for j in range(i):
                row.append(triangle[-1][j] + triangle[-1][j+1])
            row.append(1)
            triangle.append(row)
        return triangle
