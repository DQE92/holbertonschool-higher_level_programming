#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to print the value as an integer using "{:d}".format()
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Catch any errors that occur if value is not an integer
        return False
    