#!/usr/bin/python3
import json
def to_json_string(my_obj):
    """
    Converts a Python object into a JSON string.

    Parameters:
    my_obj (any): The Python object to convert (e.g., dictionary, list, string).

    Returns:
    str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
