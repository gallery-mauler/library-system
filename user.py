# user.py
class User:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def display_info(self):
        print(f"User: {self.name}")

    def checkout_book(self, book):
        print(f"{self.name} checked out {book.title}")
        self.checked_out_books.append(book)

    def return_book(self, book):
        print(f"{self.name} returned {book.title}")
        self.checked_out_books.remove(book)
