
"""
pythonの標準ライブラリを利用する実装例。
Pythonでiteratorを実祖する場合は基本的に
標準ライブラリを使用した方が良い。
"""

from collections.abc import Iterator, Iterable


class Book:
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name


# Concrete Aggregate
class BoookShelf(Iterable):
    def __init__(self) -> None:
        self._books = []

    def append_book(self, book: Book):
        self._books.append(book)

    def get_book_at(self, index):
         return self._books[index]
    
    def __iter__(self) -> Iterator:
        """
        ループ分の際にIterratorとして回してくれる
        """
        return BoookShelfIterator(self)
    
    def get_iterator(self):
        return BoookShelfIterator(self)
    
    def get_reverse_iterator(self):
        return BoookShelfIterator(self, reverse=True)


# Concrete Iterator
class BoookShelfIterator(Iterator):
    def __init__(self, book_shelf:  BoookShelf, reverse = False) -> None:
        self._book_shelf = book_shelf
        self._reverse = reverse
        if reverse:
            self._index = -1
        else:
            self._index = 0 

    def __next__(self) -> Book:
        """
        loopで回される時に、この関数が実行される。
        Iteratorが値を返す処理と、終了する処理の実装がこの中で必要
        """
        try:
            book = self._book_shelf.get_book_at(self._index)
            if self._reverse:
                self._index += -1
            else:
                self._index += 1
        except IndexError:
            # リストの数を超えて参照してしまった場合のエラーハンドリングとして
            # __next__の処理を停止するような信号を呼び出し元に返す
            raise StopIteration()

        return book


book_shelf = BoookShelf()
book_shelf.append_book(Book("OnePiece 1"))
book_shelf.append_book(Book("OnePiece 2"))
book_shelf.append_book(Book("OnePiece 3"))
book_shelf.append_book(Book("OnePiece 4"))
book_shelf.append_book(Book("OnePiece 5"))

for book in book_shelf:
    print(book.get_name())

print("=====================================")

for book in  book_shelf.get_iterator():
    print(book.get_name())

print("=====================================")
# 逆順で出力
book_shelf_reverse_iterator = book_shelf.get_reverse_iterator()
for book in book_shelf_reverse_iterator:
    print(book.get_name())

