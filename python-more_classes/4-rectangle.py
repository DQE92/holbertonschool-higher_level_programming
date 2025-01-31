#!/usr/bin/python3
"""
Class that defines a rectangle with width and height
"""

class Rectangle:

    def __init__(self, width=0, height=0):
        """Class constructor with default values"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
      
    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)), or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: A string representation of the rectangle, or an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: A string in the format "Rectangle(width, height)" 
             that allows recreating the object using eval().
        """
        return f"Rectangle({self.width}, {self.height})"
