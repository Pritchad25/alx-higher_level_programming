#!/usr/bin/python3

def safe_print_list_integers9my_list=[], x=0):

    """This function prints the first x elements
    of a list and only integers.

    Args:
    x (int): the number of elements of my_list
    to print
    my_list (list): the list from which to print elements

    Returns:
    The real number of integers printed
    """
    a = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            a += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (a)
