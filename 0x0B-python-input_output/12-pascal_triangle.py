#!/usr/bin/python3
"""Definition of a Pascal's Triangle function."""


def pascal_triangle(n):
    """This method represents Pascal's Triangle of size n.
	The method returns a list of lists of integers representing
	the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
