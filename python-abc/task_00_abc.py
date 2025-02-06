#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""
    
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Concrete class representing a Dog, inheriting from Animal."""
    
    def sound(self):
        """Returns the sound a dog makes."""
        return ("Bark")


class Cat(Animal):
    """Concrete class representing a Cat, inheriting from Animal."""
    
    def sound(self):
        """Returns the sound a cat makes."""
        return ("Meow")
    