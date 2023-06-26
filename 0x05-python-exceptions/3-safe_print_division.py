#!/usr/bin/python3

def safe_print_division(a, b):
    """This function divides two integers and
    returns or prints the result."""
    try:
        divInt = a / b
    except (TypeError, ZeroDivisionError):
        divInt = None
    finally:
        print("Inside result: {}".format(divInt))
    return (divInt)
