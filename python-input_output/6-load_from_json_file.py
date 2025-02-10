#!/usr/bin/python3
import json
def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Parameters:
    filename (str): The name of the file containing the JSON data.

    Returns:
    any: The Python object corresponding to the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
