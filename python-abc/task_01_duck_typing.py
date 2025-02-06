#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle with given radius"""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the circle"""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        """Initialize rectangle with given width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of the given shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
