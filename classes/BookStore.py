class BookStore():
    def __init__(self):
        self.books = {}

    def add_book(self, name, price):
        self.books[name] = price

    def remove_book(self, name):
        self.books.pop(name)

    def print_books(self):
        print(self.books)

class BookStoreSales():
    def __init__(self, bs):
        self.books = bs
        self.total_income = 0
        self.sold_books = []

    def sell_book(self, name):
        self.total_income += self.books[name]
        self.sold_books.append(name)
        self.books.pop(name)

    def print_total_income(self):
        print(self.total_income)

Aubreys = BookStore()
AubreysSales = BookStoreSales(Aubreys.books)

Aubreys.add_book("Tales of Elysia", 1000)
Aubreys.add_book("Tales of Umbrus", 500)
Aubreys.print_books()
AubreysSales.sell_book("Tales of Umbrus")
Aubreys.print_books()
print(AubreysSales.sold_books)