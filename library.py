# library.py
from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            book.display_info()

    def display_users(self):
        print("Library Users:")
        for user in self.users:
            user.display_info()
