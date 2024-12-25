
from abc import ABC, abstractmethod

"""
WriteAbstractionインターフェースを継承したクラスの機能追加があっても
Shapeインターフェースを継承したクラスに影響を与えない。
保守性が高くなる。
"""

class Shape(ABC):
    def __init__(self, width, heigt) -> None:
        self._width = width
        self._heigt = heigt
    @abstractmethod
    def create_shepe_str(self):
        pass

class RectangeSpahe(Shape):
    def __init__(self, width, heigt) -> None:
        super().__init__(width, heigt) 

    def create_shepe_str(self):
        rectangle =  "*" * self._width + "\n"
        for _ in range(self._heigt -2):
            rectangle += "*" + " " * (self._width -2) + "*" + "\n"

        rectangle += "*" * self._width + "\n" 
        return rectangle
    
class SquareShape(Shape):
    def __init__(self, width, heigt = None) -> None:
        super().__init__(width, heigt)

    def create_shepe_str(self):
        rectangle =  "*" * self._width + "\n"
        for _ in range(self._width -2):
            rectangle += "*" + " " * (self._width -2) + "*" + "\n"

        rectangle += "*" * self._width + "\n" 
        return rectangle


class WriteAbstraction(ABC):
    def __init__(self, shape: Shape) -> None:
        self._shape = shape

    def read_shape(self):
        return self._shape.create_shepe_str()
    
    @abstractmethod
    def write_to_text(self):
        pass


class WriteShape(WriteAbstraction):
    def write_to_text(self, filename):
        with open(file=filename, mode="w", encoding="utf-8") as f:
            f.write(self.read_shape())



rectangle = RectangeSpahe(10,5)
print(rectangle.create_shepe_str())

sqare = SquareShape(19)
print(sqare.create_shepe_str())

# bridgeパラーンを利用した機能追加例
write_shape = WriteShape(rectangle)
write_shape.write_to_text("tmp.txt")



