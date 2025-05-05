# Innovated the Assignment 9 with Shape Calculator.
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Shape calculator
def shape_calculator():
    print("Welcome to Shape Area Calculator!")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    choice = input("Choose a shape (1/2/3): ")

    if choice == "1":
        w = float(input("Enter Width: "))
        h = float(input("Enter Height: "))
        shape = Rectangle(w, h)

    elif choice == "2":
        r = float(input("Enter Radius: "))
        shape = Circle(r)

    elif choice == "3":
        b = float(input("Enter Base: "))
        h = float(input("Enter Height: "))
        shape = Triangle(b, h)

    else:
        print("Invalid Choice.")
        return

    print(f"Area: {shape.area():.2f}")

# Run the calculator
shape_calculator()