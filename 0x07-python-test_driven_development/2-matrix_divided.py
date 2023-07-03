#!/usr/bin/python3
# 2-matrix_divided.py
"""Definition of a matrix division function."""


def matrix_divided(matrix, div):
    """This function divides all the
    elements of a matrix.

    Args:
        matrix (list): a list of lists of integers or
        floats.
        div (int/float): the divisor.

    Raises:
        TypeError: if the matrix contains non-numbers.
        TypeError: if the matrix contains rows of
        different sizes.
        TypeError: if div is not an integer or a float
        ZeroDivisionError: if div is 0.
    Returns:
        A new Matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)
        of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
