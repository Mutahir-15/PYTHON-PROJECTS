# Assignment: Static Method

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/3) + 32
    
# Using it here
temp_c = 32
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}*C equals to {temp_f}*F.")

# Understanding concepts
"""
What is @staticmethod?
@staticmethod means the method doesn't need access to self or cls.
We can call it directly using class name, without creating an object.

In the previous assignments, we created objects to interact with class methods. 
However, in this case, we're using a static method, which allows us to call the method
directly using the class name, without creating any object.
"""