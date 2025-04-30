# Assignment: Public Variables and Methods

class Car:
    def __init__(self, brand):

        # Public Variable
        self.brand = brand

    # Public Method
    def start(self):
        print(f"The {self.brand} has started.")

# Creating an object of Car
car1 = Car("TOYOTA")
print("Brand:", car1.brand)

# Calling public Method
car1.start()

# Understanding Concepts.
"""
What is Public Variable?
Public variable is fully open and can be accessed anywhere.

What is Public Method? 
Public Method is also fully open and can be called outside the class.

NO SPECIAL SYMBOL IS NEEDED JUST DEFINED NORMALLY.
"""