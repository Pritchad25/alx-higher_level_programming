#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """This function divides 2 lists element
    by element

    Args:
    my_list_1 (list): the first list
    my_list_2 (list): the second list
    list_length (int): the total number of elements
    to divide

    Returns:
    A new list that is of length list_length
    containing all the divisions"""
    newList = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            newList.append(div)
    return (newList)
