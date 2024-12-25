
from abc import ABC, abstractmethod


# abstract class
class AbstractDisplay(ABC):
    def display(self):
        self._open()
        for i in range(5):
            self._print()
        self._close()
        self._addtitional_method()

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _close(self):
        pass

    @abstractmethod
    def _print(self):
        pass

    def _addtitional_method(self):
        """継承先で実装しても実装しなくても問題ないメソッド"""
        pass


# concrete class
class CharDisplay(AbstractDisplay):
    def __init__(self, char) -> None:
        self._charactor = char

    def _open(self):
        print('<<', end='')

    def _print(self):
        print(self._charactor, end='')
        
    def _close(self):
        print('>>')

    def _addtitional_method(self):
        print("Additional method is called.")


class StringDisplay(AbstractDisplay):
    def __init__(self, msg) -> None:
        self._msg = msg

    def _open(self):
        self._print_line()

    def _print_line(self):
        print("+" + "-" * len(self._msg) + "+" )

    def _print(self):
        print("|" + self._msg + "|")

    def _close(self):
        self._print_line()




c_display = CharDisplay("*")
c_display.display()

print("=" * 7)

s_display = StringDisplay("hello world")
s_display.display()









