#!/usr/bin/python3
""" Nameless module containing Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class.
    """

    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        Rectangle.integer_validator(self, "size", size)

        self.__size = size

    def area(self):
        """Calculates area of the Square

            Returns:
                Area
        """

        return self.__size * self.__size

    def __str__(self):
        """Stringify the dimensions of the square.

            Returns:
                String describing Square's dimensions
        """

        return "[Square] " + str(self.__size) + "/" + str(self.__size)
