#!/usr/bin/python3
import json
"""
    Converts a JSON string into a Python object.

    Parameters:
    my_str (str): A string containing JSON data.

    Returns:
    any: The corresponding Python object (e.g., list, dictionary, string, etc.).
    """
def from_json_string(my_str):
    return json.loads(my_str)
