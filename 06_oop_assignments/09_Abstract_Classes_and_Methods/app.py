# Assignment: Abstract Classes and Methods
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # Pass means no implementation here

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Here if we do shape = Shape() it will raise error: can't initiate abtract class
rect = Rectangle(20,30)
print(f"The Area of Rectangle is: ", rect.area())

# Understanding Concepts
"""
What is Abstract Class?
An abstract class cannot be instantiated.
It may contain abstract methods that must be implemented by any subclass.

What is abc module?
Abstraction is handled using the abc module.
We use the abc module and @abstractmethod decorator to define them.
"""