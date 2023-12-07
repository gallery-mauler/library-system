# main.py
from book import Book
from user import User
from library import Library

# Create books
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Create users
user1 = User("Alice")
user2 = User("Bob")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Add users to the library
library.add_user(user1)
library.add_user(user2)

# Display library information
library.display_books()
library.display_users()

# Simulate user actions
user1.checkout_book(book1)
user2.checkout_book(book2)

# Display updated library information
library.display_books()
library.display_users()
