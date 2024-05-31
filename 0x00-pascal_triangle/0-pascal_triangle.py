#!/usr/bin/python3
"""This module contains a function that returns a list of lists
 of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers for the Pascal’s triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
