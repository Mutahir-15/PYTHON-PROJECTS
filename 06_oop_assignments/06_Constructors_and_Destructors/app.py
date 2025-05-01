# Assignment: Constructor and Destructor.

class Logger:
    # Constructor
    def __init__(self):
        print("Logger initialized. An object was created.")

    # Destructor
    def __del__(self):
        print("Logger destroyed. Object is deleted.")

# Calling the Constructor
log = Logger()

# Calling the destructor
del log

# Understanding Concepts
"""
What is Constructor?
Constructor function runs when the object is created.

What is Destructor?
It runs when the object is destroyed.
"""