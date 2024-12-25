
from abc import ABC, abstractmethod

"""
よくある実装パターン
"""

class Book:
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name

 
class Aggregate(ABC):
    @abstractmethod
    def iterator(self):
        pass

# Concrete Aggregate
class BookShelf(Aggregate):
    def __init__(self) -> None:
        self._books = []

    def append_book(self, book: Book):
        self._books.append(book)
    
    def get_book_at(self, index):
        return self._books[index]
    
    def iterator(self):
        return BookShelfIterator(self)
    
    def __len__(self):
        return len(self._books)


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

# Concrete Iterator
class BookShelfIterator(Iterator):
    def __init__(self, book_shelf: BookShelf ) -> None:
        self._bookshelf = book_shelf
        self._index = 0

    def has_next(self):
        if self._index < len(self._bookshelf):
            return True
        else:
            return False
        
    def next(self):
        book = self._bookshelf.get_book_at(self._index)
        self._index += 1
        return book


book_shelf = BookShelf()
book_shelf.append_book(book = Book("one piece 1"))
book_shelf.append_book(book = Book("one piece 2"))
book_shelf.append_book(book = Book("one piece 3"))
book_shelf.append_book(book = Book("one piece 4"))

book_iterator = book_shelf.iterator()

while(True):
    if book_iterator.has_next():
        print(book_iterator.next().get_name())
    else:
        break

