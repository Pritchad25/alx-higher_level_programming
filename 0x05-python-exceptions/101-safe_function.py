#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """This function executes a function safely

    Args:
    fct- the pointer to the function to execute
    args- the arguments for fct or for the function

    Return:
    None- if an error occurs during function execution
    Otherwise, the result of the function"""

    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
