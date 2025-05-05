# Assignment: Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self.price = price      # Private attribute

    # Getter
    @property
    def price(self):
        print("Getting the price...")
        return self.price

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting the price...")
            self._price = value

    # Deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Example usage
item = Product(100)
print(item.price)       # Getting the price
item.price = 150        # Setting the price
print(item.price)
del item.price          # Deleting the price

# Understaing concepts
"""
What are Property Decorators?
1.  @property: Allows access to _price like a public attribute while keeping it private internally.
2.  @price.setter: Validates or controls how _price is updated.
3.  @price.deleter: Defines how the attribute is deleted safe.
"""