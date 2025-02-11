#!/usr/bin/python3

class Student:
    """
    A class that defines a student with first name, last name, and age.
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initialize a student instance.
        :param first_name: First name of the student.
        :param last_name: Last name of the student.
        :param age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        :param attrs: List of attribute names to retrieve.
        :return: Dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
