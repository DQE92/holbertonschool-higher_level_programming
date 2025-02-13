#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save the data.

    Returns:
        None
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
