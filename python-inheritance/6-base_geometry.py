#!/usr/bin/python3
class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """
        Method that should calculate the area.
        However, it is not yet implemented.
        Instead, it raises an exception to enforce implementation in subclasses.
        """
        raise Exception("area() is not implemented")