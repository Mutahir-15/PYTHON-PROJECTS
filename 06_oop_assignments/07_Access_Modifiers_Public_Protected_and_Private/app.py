# Assignment: Access Modifiers: Public, Protected, and Private.

class Employee:
    def __init__(self, name , salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected
        self.__ssn = ssn        # Private
        
    def display(self):
        print(f"Name (Public): {self.name}")
        print(f"Salary (Protected): {self._salary}")
        print(f"SSN (Private): {self.__ssn}")

emp = Employee("Mutahir Bin Athar", 100000, "147-852-369")

# Accessing Public
print("Public name:", emp.name)

# Accessing Protected (allowed, but not recommended directly)
print("Protected Salary:", emp._salary)

# Accessing Private (will cause error)
try:
    print("Private SSN:", emp.ssn)
except AttributeError as e:
    print("Error accessing private variable:",e)

# Accessing private variable using name mangling (not recommended but possible)
print("Accessing Private SSN via name mangling:", emp._Employee__ssn)


# Understanding Concepts
"""
What is public, protected and private variables?
Public: "name", accessable any where.
Protected: "_salary", conventionally for internal use.
Private: "__ssn", Name mangles (harder to use).

What is name mangling?
Name mangling is a mechanism used in Python to make private variables harder to access from outside the class.
"""