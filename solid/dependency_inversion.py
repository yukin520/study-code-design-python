

"""
良い例。
このよう抽象化クラスを継承してクラスを定義することで、
そのクラスを利用するモジュールの拡張がしやすい。
（抽象化クラスのインターフェースを満たすクラスを追加すればOKなため）
"""

from abc import ABCMeta, abstractmethod

class IBook(metaclass = ABCMeta):
        @property
        @abstractmethod
        def content(self):
             pass
        
class Book(IBook):
    def __init__(self, content:str) -> None:
        self._content = content

    @property
    def content(self):
         return self._content

class IFormatter(metaclass = ABCMeta):
        @classmethod
        @abstractmethod
        def format(self, ibook:IBook):
             pass
        
class HtmlFormatter(IFormatter):
    def format(self, i_book:IBook):
        return '<h1>' + i_book.content + '</h1>'
    

class TextFormatter(IFormatter):
    def format(self, i_book:IBook):
        return i_book.content


class Printer:
    def __init__(self, i_formatter:IFormatter) -> None:
         self.i_formatter = i_formatter

    def print(self, ibook:IBook):
        formatterd_book = self.i_formatter.format(ibook)
        print(formatterd_book)

book = Book("My book")

html_formatter = HtmlFormatter()
html_printer = Printer(html_formatter)
html_printer.print(book)

# 簡単に拡張可能
text_formatter = TextFormatter()
text_printer = Printer(text_formatter)
text_printer.print(book)





# ============================================================
# '''
# 好ましくない例
# このような例ではFormatterAのようなFormatterを拡張した
# ものを追加する場合、Printerを修正する必要が出てきしまう。
# '''

# class Book:
#     def __init__(self, content) -> None:
#         self.content = content

# class Formatter:
#     def format(self, book:Book):
#         return book.content
    
# class Printer:
#     def print(self, book: Book):
#         formatter = Formatter()
#         formatterd_book = formatter.format(book)
#         print(formatterd_book)


# book = Book("My book")
# printer = Printer()
# printer.print(book)


# class FormatterA:
#     '''
#     このような別のFormatterクラスを作成した場合、
#     Printerクラスに追加するのが手間。
#     '''
#     def format(self, book:Book):
#         return book.content + "A"
        