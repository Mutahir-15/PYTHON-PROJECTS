# Assignment: Class Methods

class Book:
    total_books = 0     # Class variable to check total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()     # Call class method when the book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
# Creating objects for Books
book1 = Book("Deewan e Ghalib - Mirza Asad Ullah Khan Ghalib")
book2 = Book("Zindan Nama - Faiz Ahmad Faiz")
book3 = Book("Shayad - John Elia")

# Displaying total number of books
print(f"Total books added: {Book.get_total_books()}")

# Understanding concepts
"""
What are @classmethods?
@classmethod allows the method to access/modify the class state (cls refers to the class).
"""