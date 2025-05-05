# Assignment: Decorators

def log_functoion_call(func):
    def wrapper():
        print("Functuion is being called.")
        return func()
    return wrapper
    
# Function to Decorate.
@log_functoion_call
def say_hello():
    print("Hello!")

# Calling the function
say_hello()

# Understanding concepts
"""
What is Decorator?
1.  A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
2.  Here, @log_function_call is applied to say_hello(), so it prints a message before calling the actual function.
"""