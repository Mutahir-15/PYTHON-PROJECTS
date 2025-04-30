# Assignment: Class Variables and Methods

class Bank:
    # Class variable
    bank_name = "HBL"
    def __init__(self, account_holder):
        self.account_holder = account_holder    # Instance variable

    @classmethod
    def change_bank_name(cls, bank_name):
        cls.bank_name = bank_name   # Changes the class variable for All instances
    
    def show_details(self):
        print(f"Account holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Creating an objects
acc1 = Bank("Imran Khan")
acc2 = Bank("Mutahir Bin Athar")

# Showing initials bank names
acc1.show_details()
acc2.show_details()

# Changing bank name using class method
Bank.change_bank_name("Meezan Bank")

# Showing updated bank names    
acc1.show_details()
acc2.show_details()

# Understanding Concepts.
"""
What is Class Variable?
A class variable is Shared by all objects.

What is Class Method? 
Class method Can access/change class variables using cls.
"""