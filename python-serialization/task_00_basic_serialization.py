#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    If the file already exists, it will be replaced.
    
    :param data: Dictionary containing data to serialize
    :param filename: Name of the JSON file to save data
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.
    
    :param filename: Name of the JSON file to read
    :return: Deserialized Python dictionary
    """
    with open(filename, 'r') as file:
        return json.load(file)
