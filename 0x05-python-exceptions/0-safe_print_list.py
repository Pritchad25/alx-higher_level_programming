#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """This function prints x elements of a list.

    Args:
    x(int): The number of elements of my_list to print
    my_list (list): the list from which elements are
    to be printed.

    Returns: The real number of elements printed.
    """

    elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elem += 1
        except IndexError:
            break
    print("")
    return (elem)
