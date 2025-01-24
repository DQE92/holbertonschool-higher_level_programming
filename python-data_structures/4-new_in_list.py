#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Check if the index is within range
    if 0 <= idx < len(my_list):
        # Replace the element at the specified index
        new_list[idx] = element
    
    # Return the new list (unchanged if index is invalid)
    return new_list
