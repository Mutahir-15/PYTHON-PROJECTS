# Assignment: Using cls

class Counter:
    count = 0
    def __init__(self):

        # It increments the class variable when an object is created. 
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects are: {cls.count}")

# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()

# Understanding Concepts.
"""
What is cls?
cls is a reference to the class itself, used in class methods.
"Keep in mind": Instance variable (self.x) → Belongs to one object.

What is @classmethod? 
@classmethod is used to define a method that belongs to the class, not the instance.
"""