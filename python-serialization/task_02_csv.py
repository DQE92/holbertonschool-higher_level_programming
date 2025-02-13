#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(file_csv):
    """
    Converts a CSV file to a JSON file.

    Args:
        file_csv (str): The path to the CSV file.

    Returns:
        bool: True if the conversion is successful, False otherwise.
    """
    try:
        with open(file_csv, 'r') as cfile:
            csv_read = csv.DictReader(cfile)
            data = [row for row in csv_read]

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return False
