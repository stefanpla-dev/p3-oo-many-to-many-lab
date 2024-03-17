class Author:
    all = []
    def __init__(self, name):
        self._name = ""
        self.name = name #create an author class that has the following attributes: name (string)
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self): # was get_contracts, returns a list of contracts related to the author.
        return [contract for contract in Contract.all if contract.author is self]
        # result = []
        # for contract in Contracts.all:
        #     if contract.author is self:
        #         result.append(contract)
        # return result

    def books(self): # was get_books, returns a list of contracts related to the author. Contract class is the intermediary.
        return [contract.book for contract in Contract.all if contract.author is self] # was 
        # result = []
        # for contract.book in Contract.all:
        #     if contract.author is self:
        #         result.append(book)
        # return result

    def sign_contract(self, book, date, royalties): #method should create and return a new Contract object between the author and the specified book and the specified date and royalties.
        return Contract(self, book, date, royalties)

    def total_royalties(self): #this method should return the total amount of royalties that the author has earned from all of their contracts
        #return sum(Contract.all.royalties) -> this was getting an attirbute error that basically the thing I'm trying to sum isn't a list. Need to sum some other way
        
        # total = 0 
        # for contract.royalties in Contract.all: # use Contract as intermediary
        #     if ontract.author is self:
        #         total += contract.royalties
        # return total -> idk why this wasn't working

        return sum([contract.royalties for contract in Contract.all if contract.author is self]) 


class Book: 
    all = []
    def __init__(self, title):
        self._title = title #create a Book class that has the following attributes: title (string)
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value
    
    def contracts(self): # think of as get_contracts
        return [contract for contract in Contract.all if contract.book is self] 
        # result = []
        # for contract in Contract.all:
        #     if contract.book is self:
        #         result.append(contract)
        # return result
    
    def authors(self): # think of as get_authors
        return [contract.author for contract in Contract.all if contract.book is self]
        # result = []
        # for contract in Contract.all:
        #     if contract.book is self:
        #         result.append(contract.author)
        # return result

class Contract:
    all = []
    def __init__(self, author, book, date, royalties): # interesting error originally encountered - was ordered author, book, royalties, date, but this was throwing an error that a test for royalties was being passed in as a date, which is to say that the order of the args does matter even if none have default values.
    #validation for date and royalties below, property getters/setters
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        #create a Contract class that has the following properties: author (Author object), book (Book object), date(string) and royalties (int)
    
    @classmethod
    def contracts_by_date(cls, date): #this method should return all contracts that have the same date as the date passed into the method.
        return [contract for contract in Contract.all if contract.date is date]
        # result = []
        # for contract in Contract.all:
        #     if contract.date is date:
        #         result.append(contract)
        # return result

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):#author property has to be an instance of the Author class. same for book property below. 
            raise Exception("Author must be an instance of the Author class")
        self._author = value 

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class")
        self._book = value

    @property
    def date(self):
        return self._date

    @ date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Royalties must be a number")
        self._royalties = value