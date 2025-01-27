#!/usr/bin/python3
"""Module defining a Square class.

This module contains a simple definition of a `Square` class,
with a constructor to initialize the size of a square.
"""

class Square:
    """Class representing a square.

    Attributes:
        __size (int): The size of the square's side (private).
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
