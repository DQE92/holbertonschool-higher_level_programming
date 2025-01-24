#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The list of integers to check.

    Returns:
        list: A list of True or False corresponding to whether each integer
              in the input list is divisible by 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
