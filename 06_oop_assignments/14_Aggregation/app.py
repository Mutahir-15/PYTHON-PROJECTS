# Assignment: Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

# Creating a class using Aggregation
class Department:
    def __init__(self, depart_name, employee):
        self.depart_name = depart_name
        self.employee = employee        # Aggregation: Department has a reference to an existing Employee

    def show_details (self):
        print(f"Department: {self.depart_name}")
        self.employee.show()        # Accessing employee method

# Creating an object for employee independently
emp1 = Employee("Mutahir")

# Now passing this employee obj to the Department
dep1 = Department("Agentic AI", emp1)

# Showing Department details
dep1.show_details()

# Understaing concepts
"""
What is Aggregation?
Aggregation is a type of association where one class holds a reference to another class, but both can exist independently.
If the department is deleted, the employee still exists.
View (Line number: 14).

Difference between Composition and Aggregation:
The key difference b/w compostion and aggregation is that in composition, the contained object depends on the container (strong binding),
while in aggregation, it can exist independently (loose binding). 
"""