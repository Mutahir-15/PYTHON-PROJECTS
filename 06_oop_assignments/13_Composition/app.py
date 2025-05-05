# Assignment: Composition

class Engine:
    def start(self):
        print("Engin has started.")

# Class Car using Composition
class Car:
    def __init__(self, engine):
        self.engine = engine    # Composition: Cas has an Engin.

    def start_car(self):
        print("Starting the engine...")
        self.engine.start()     # Accessing Engin's method

# Creating an onject for the engin
engine1 = Engine()

# Now passing the Engine onject to the class Car
car1 = Car(engine1)

# Using Car to start the engine
car1.start_car()

# Understanding concepts
"""
What is Composition?
Composition is a design principle where one class contains an object of another class
to build a complex functionality.

It represents a (has-a) relationship.
What we did here:
A Car has-an Engine. 
View (Line number: 10).
"""