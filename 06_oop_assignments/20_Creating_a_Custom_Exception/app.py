# Assignment: Creating a Custom Exception

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError
    else:
        print("Access granted.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid number.")

# Understanding concepts
"""
Creating Custom Expection:
1.  A custom exception helps clearly define domain-specific errors.
2.  raise InvalidAgeError triggers it manually if the condition is met.
3.  It’s caught using try...except just like built-in exceptions.
"""