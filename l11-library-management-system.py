"""
Design a Library Management System.
Users can borrow and return books. The system should track borrowed books,
availability status, and handle due dates and fines.

Actors:
    -> library system
    -> book
    -> user
    -> borrow

"""
from datetime import datetime, timedelta
from uuid import uuid4


class BookCopy:
    def __init__(self, book_id, name, author):
        self.id = str(uuid4())
        self.book_id = book_id
        self.name = name
        self.author = author
        self.is_available = True

    def mark_borrowed(self):
        self.is_available = False

    def mark_returned(self):
        self.is_available = True


class Book:
    def __init__(self, name, author):
        self.id = str(uuid4())
        self.name = name
        self.author = author
        self.copies = []

    def add_copies(self, n):
        for _ in range(n):
            self.copies.append(BookCopy(self.id, self.name, self.author))


class Borrowing:
    def __init__(self, user, book, due_date, fine_amount):
        self.user = user
        self.book = book
        self.due_date = due_date
        self.fine_amount = fine_amount
        self.timestamp = datetime.now()


class LibrarySystem:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.borrow_history = []
        self.borrowings = []

    def add_book(self, name, author):
        book = Book(name=name, author=author)
        self.books.append(book)
        return book

    def list_books(self):
        return self.books

    def borrow_a_book(self, book_copy, user, due_date=datetime.now() + timedelta(days=5), fine_amount=100):
        if not book_copy.is_available:
            raise Exception("Book unavailable")
        self.borrow_history.append((book_copy, user, datetime.now(), due_date))
        book_copy.mark_borrowed()
        self.borrowings.append(Borrowing(user, book_copy, due_date, fine_amount))

    def accept_return(self, book_copy, user):
        book_copy.mark_returned()
        for b in self.borrowings:
            if b.book.id == book_copy.id and b.user.id == user.id:
                self.borrowings.remove(b)
                if datetime.now() > b.due_date:
                    overdue_days = (datetime.now() - b.due_date).days
                    print(f"Fine to be paid: ₹{overdue_days * b.fine_amount}")
                break

    def availability_status(self, book_copy):
        return book_copy.is_available


class User:
    def __init__(self, name):
        self.id = str(uuid4())
        self.name = name
        self.borrowed_book = []

    def borrow_book(self, library_system, book_copy):
        library_system.borrow_a_book(book_copy, self)
        self.borrowed_book.append(book_copy)

    def return_book(self, library_system, book_copy):
        library_system.accept_return(book_copy, self)
        self.borrowed_book.remove(book_copy)
