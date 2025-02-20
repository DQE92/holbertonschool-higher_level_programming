#!/usr/bin/python3
"""
This module contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        