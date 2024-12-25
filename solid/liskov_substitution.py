

"""
リスコフの置換原則を満たして実装した例
"""


class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def  width(self):
        return self.width

    @width.setter
    def width(self,width):
        self._width = width
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self,height):
        self._height = height

    def calcurate_area(self):
        return self._width * self._height
    

class Square(Rectangle):
    def __init__(self,size) -> None:
        self._width = size
        self._height = size

    @Rectangle.width.setter
    def width(self,size):
        self._width = size
        self._height = size

    @Rectangle.height.setter
    def height(self,size):
        self._width = size
        self._height = size


def print_area(obj):
    changed_to_width = 10
    changed_to_height = 20

    obj.width = changed_to_width
    obj.height = changed_to_height

    if isinstance(obj, Square):
        """
        この判定がないとSquareの時に予想面積と結果面積が異なってしまい（振る舞いが異なってしまい）、
        スーパークラスであるRectangleの代用とならない。
        リスコフの置換原則を満たさないとみなされてしまう。
        
        ただ、この処理はかなり強引な方法。より良い実装があるはず
        """
        changed_to_width = changed_to_height

    print(f"予想面積={ changed_to_height * changed_to_width}, 結果面積 = {obj.calcurate_area() }")



rc = Rectangle(2, 3)
print_area(rc)

sq = Square(5)
print_area(sq)



