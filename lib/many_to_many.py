class Author:
    # Class variable to keep track of all Author instances
    all_authors = []

    def __init__(self, name):
        self.name = name
        # Add the current instance to the class variable list
        Author.all_authors.append(self)
        self._contracts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid input types.")
        if royalties < 0 or royalties > 100:
            raise Exception("Royalties must be between 0 and 100.")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)



class Book:
    # Class variable to keep track of all Book instances
    all_books = []

    def __init__(self, title):
        self.title = title
        # Add the current instance to the class variable list
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        self._title = value


class Contract:
    # Class variable to keep track of all Contract instances
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid input types.")
        if royalties < 0 or royalties > 100:
            raise Exception("Royalties must be between 0 and 100.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # Add the current instance to the class variable list
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an Author object.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be a Book object.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            raise Exception("Royalties must be an integer between 0 and 100.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]