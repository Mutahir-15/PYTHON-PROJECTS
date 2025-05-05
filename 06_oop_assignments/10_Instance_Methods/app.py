# Assignment: Instance Method

class Dog:
    def __init__(self, name, breed):
        self.name = name        # Instace variable
        self.breed = breed      # Instance variable

    def bark(self):     # Instnce method
        print(f"{self.name} who is a {self.breed} says: Woof Woof!")

    def sit(self):      # Instance method
        print(f"{self.name} is not sitting!")

# Creating object of a Dog class
dog1 = Dog("Jackie", "Cane Corso")

# Calling the instance methods
dog1.bark()
dog1.sit()

# Understanding concepts
"""
What is Instance Variable?
An Instance variable is a variable that is defined inside a class but outside any method, and it is unique
to each (object) of the class.
"""