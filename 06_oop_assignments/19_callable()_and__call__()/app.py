# Assignment: callable() and __call__()

from typing import Any


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

# Creating an instance of Multiplier
double = Multiplier(2)

# Check if object is callable
print("Is 'double' callabel?", callable(double))    # Output: True

# Use the object like a function
result = double(10)     # Calls __call__(10)
print("Result of double(10):", result)

# Understanding concepts
"""
What is callable() method?
1.  __call__() lets you treat the object like a function.
2.  callable(obj) checks if an object can be called (i.e., has __call__() defined).
"""