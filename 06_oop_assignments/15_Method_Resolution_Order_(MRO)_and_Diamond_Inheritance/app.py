# Assignment: Method Resolution Order (MRO) and Diamond Inheritance

# Base class A
class A:
    def show(self):
        print(f"Showing from class A.")

# class B inherits from A
class B(A):
    def show(self):
        print(f"Showing from class B.")

# class C inhertis from A
class C(A):
    def show(self):
        print(f"Showing from C.")

# class D inherits from both B and C
class D(B,C):
    def show(self):
        pass

# Creating an object of class D
d = D()

# This will follow Method Resolution Order (MRO)
d.show()

# Understading concepts
"""
What is (MRO)?
MRO stand for: Method Resolution Order.
This defins the order in which the base classes are searched when executing a method.

What is Diamond Inheritance?
1.  First lets understand what is Inheritance: 
    Inheritance allows a class to inherit attributes and methods from another class (parent → child).
2.  Multiple Inheritance is known as Diamond Inheritance.
"""