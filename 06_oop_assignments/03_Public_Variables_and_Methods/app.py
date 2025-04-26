# Assignment: Public Variables and Methods

class Car:
    def __init__(self, brand):

        # Public Variable
        self.brand = brand

    # Public Method
    def display_brand(self):
        print(f"{self.brand} is my favourite car Brand.")

# Creating an object of Car
car1 = Car("TOYOTA")
print("Brand:", car1.brand)

# Calling public Method
car1.display_brand()

# Understanding Concepts.
"""
What is Public Variable?
Public variable is fully open and can be accessed anywhere.

What is Public Method? 
Public Method is also fully open and can be called outside the class.

NO SPECIAL SYMBOL IS NEEDED JUST DEFINED NORMALLY.
"""