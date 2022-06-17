class Bookstore():
    def __init__(self):
        self.books = {}

    def add_book(self, name, price):
        self.books[name] = price

    def remove_book(self, name):
        self.books.pop(name)

    def print_books(self):
        print(self.books)

Aubreys = Bookstore()

Aubreys.add_book("Tales of Elysia", 1000)
Aubreys.add_book("Tales of Umbrus", 500)
Aubreys.print_books()
Aubreys.remove_book("Tales of Umbrus")
Aubreys.print_books()