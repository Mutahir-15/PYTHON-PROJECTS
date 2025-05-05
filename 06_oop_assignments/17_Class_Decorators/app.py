# Assignment: Class Decorators

def add_greetings(cls):
    # Adding a new method to the class
    def greet(self):
        return "Hello from Decorator!"

    cls.greet = greet
    return cls

# Now, applying the decorator to the class
@add_greetings
class Person:
    def __init__(self, name):
        self.name = name

# Creating object
p1 = Person("Mutahir")
print(p1.name)
print(p1.greet())

#  Understanding concepts
"""
What is Class Decorator?
1.  A class decorator takes a class as input, modifies it (like adding new methods), and returns the modified class.
2.  Here, add_greeting adds a new method greet() to any class it decorates.
3.  When we use @add_greeting above the Person class, it dynamically gains the greet() method.
"""