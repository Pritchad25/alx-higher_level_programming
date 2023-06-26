#!/usr/bin/python3

def list_divisison(my_list_1, my_list_2, list_length):
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
            divList = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divList = 0
        except ZeroDivisionError:
            print("division by 0")
            divList = 0
        except IndexError:
            print("out of range")
            divList = 0
        finally:
            newList.append(divList)
    return (newList)
