# Assignment: Using self

class Student:
    def __init__(self, name, marks):
        self.name = name    # This is called "Instance Variables".
        self.marks = marks  # This is called "Instance Variables".

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Creating an object of the class
student1 = Student("Mutahir", 96)

# Calling the method to display details
student1.display()

# Understanding Concepts.
"""
What is self? 
known as the Heart of OOP in Python.
"self" is basically a reference to the current object of a class. 

What is Instance Variable?
Instance variable is a variable which is "specific to each object" created form a class.
It is usually declared inside the constructor (__init__).
It is accessed using "self".
"""