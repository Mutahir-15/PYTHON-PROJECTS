# Assignment: The Super() Function

class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling parent constructor
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Suncject: {self.subject}")

teacher = Teacher("Sir Arif Rozani", "Agentic AI")
teacher.display()

# Understanding Concepts
"""
What is the Super() Function?
The super() function allows the child class to call methods (usually constructors) from its parent class.

Uses of super():
1. Reduces code duplications.
2. Reuses initialization from parent class.
3. Insure consistancy in inheritance chain (espacially in multiple inheritance).
"""