#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element by element.

    Args:
        my_list_1 (list): The first list (can contain any type).
        my_list_2 (list): The second list (can contain any type).
        list_length (int): The length of the result list.

    Returns:
        list: A new list containing the results of the division.
    """
    result = []
    for i in range(list_length):
        try:
            # Ensure indexes are within range
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            # Attempt the division
            result.append(val1 / val2)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            # Finally block can be used if there's any cleanup, though not needed here
            pass

    return result