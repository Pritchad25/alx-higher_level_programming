#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Definition of a matrix multiplication
function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """This function returns the multiplication
    of two matrices.

    Args:
        m_a (list of lists of ints/floats): the first matrix.
        m_b (list of lists of ints/floats): the second matrix.
    """

    return (np.matmul(m_a, m_b))
