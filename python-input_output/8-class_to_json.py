#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description of an object
    with simple data structures for JSON serialization.
    """
    return obj.__dict__
