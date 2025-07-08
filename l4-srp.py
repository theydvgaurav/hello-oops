# SRP(Single Responsibility Principle) - A class should have one and only one responsibility.


"""

Code violating SRP

"""


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def save_to_db(self):
        print("Saved Book data to db")

    def export_pdf(self):
        print("Converted Book to pdf")


"""

SRP Compliant code

"""


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


class DBUtil:
    def __init__(self, book):
        self.book = book

    def save_to_database(self):
        print("Saved Book data to db")


class PDFUtil:
    def __init__(self, book):
        self.book = book

    def convert_to_pdf(self):
        print("Converted Book to pdf")
