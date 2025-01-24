#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):  # Iterate up to the specified number of elements
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                # Ignore elements that are not integers
                pass
    except IndexError:
        # Let IndexError propagate as requested if x is too large
        raise
    print()  # Print a newline after printing all integers
    return count
