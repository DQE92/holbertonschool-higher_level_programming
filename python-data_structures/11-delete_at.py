#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list of items.
        idx (int): The index of the item to remove.

    Returns:
        list: The modified list with the item at idx removed.
              If idx is out of range or negative, returns the original list.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
