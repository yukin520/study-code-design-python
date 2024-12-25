
from abc import ABC, abstractmethod


class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(ItemElement):
    def __init__(self, price, isbn):
        self._price = price
        self._isbn = isbn

    @property
    def price(self):
        return self._price
    
    @property
    def isbn(self):
        return self._isbn
    
    def accept(self, visitor):
        return visitor.visit(self)


class Fruit(ItemElement):
    def __init__(self, price, wegiht, name):
        self._price = price    # 1g単位の価格
        self._weight = wegiht  # 重さ(g)
        self._name = name

    @property
    def price(self):
        return self._price
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def name(self):
        return self._name
    
    def accept(self, visitor):
        return visitor.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, item:ItemElement):
        pass


class ShoppingVisitor(Visitor):
    def visit(self, item:ItemElement):
        """
        Bookは500円以上の場合10円引き、
        Fruitは20%offとする
        """
        if isinstance(item, Book):
            cost = item.price
            if cost > 500:
                cost += -10
            print(f"Book ISBN: {item.isbn}, cost: {cost}")
            return cost
        elif isinstance(item, Fruit):
            cost = item.price * item.weight
            cost = int(cost * 0.8)
            print(f"Fruit name: {item.name}, cost: {cost}")
            return cost


def calcurate_price(items):
    visitor = ShoppingVisitor()
    sum = 0
    for item in items: 
        sum += item.accept(visitor)
    return sum

items = [
    Book(400, "1111"),
    Book(1000, "2222"),
    Fruit(8, 20, "Banana"),
    Fruit(50, 30, "Apple"),
]

print(f"total cost: {calcurate_price(items=items)}")









