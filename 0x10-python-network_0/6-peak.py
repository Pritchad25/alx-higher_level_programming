#!/usr/bin/python3
"""
This module finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """This function finds the peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1
    """ The code below finds the peak."""
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]

