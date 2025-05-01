# Assignment: Static Variables and Methods

class Mathutils:
    @staticmethod
    def add(a,b):
        return a+b
    
# Calling the static method using class name
result = Mathutils.add(10,20)
print(f"The sum is: {result}")

# Understanding concepts
"""
What is Static Method?
Method inside a class that doesn't access self or cls (no object or class data).

1. No instance variable.
2. No class variable.
3. Just a statuic method is used.
"""