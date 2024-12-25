
from abc import ABC, abstractmethod
from random import randint

class Subject(ABC):
    """監視される側のクラス"""
    def __init__(self) -> None:
        self._number = 0
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def deatach(self, observer):
        self._observers.remove(observer)

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class NumberSubject(Subject):
    def notify(self):
        for observer in self._observers:
            # 変更後の自分自身の状態をObserverに伝える。
            # 引数でselfを渡しているのがポイント
            observer.update(self)
        
    def change_value(self):
        number = self._number
        self._number = randint(0,20)
        print(f"number chage from {number} to {self._number}")
        self.notify()

    def execute(self):
        print("Nmber Subject clled.")


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass


class GraphObserver(Observer):
    def update(self, subject: Subject):
        print(f"Graph observer: {subject._number}")
        subject.execute()


class NumberObserver(Observer):
    def update(self, subject: Subject):
        print(f"Number observer: {subject._number}")
        subject.execute()


subject = NumberSubject()
graph_obsever = GraphObserver()
number_observer = NumberObserver()

subject.attach(graph_obsever)
subject.attach(number_observer)
subject.change_value()


print("==================")
subject.deatach(observer=graph_obsever)
subject.change_value()