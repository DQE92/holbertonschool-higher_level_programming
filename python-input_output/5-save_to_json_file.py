#!/usr/bin/python3
import json
"""
    Writes an object to a text file using its JSON representation.

    Parameters:
    my_obj (any): The Python object to serialize.
    filename (str): The name of the file where the object will be saved.

    Returns:
    None
    """
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
