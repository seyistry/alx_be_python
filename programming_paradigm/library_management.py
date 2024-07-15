# Implementing Basic OOP for a Library Management System

class Book:
    _is_checked_out = False

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def book_status(self):
        return self._is_checked_out


class Library():
    _books = []

    def add_book(self, books):
        self._books.append(books)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.returned()

    def list_available_books(self):
        for book in self._books:
            if not book.book_status():
                print(f'{book.title} by {book.author}')
