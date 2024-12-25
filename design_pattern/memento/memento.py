
from abc import ABC, abstractmethod
from datetime import datetime
import pickle


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @property
    @abstractmethod
    def date(self):
        pass


class ConcreteMement(Memento):
    def __init__(self, state, name) -> None:
        self._name = name
        self._state = state
        self._date = datetime.now()

    @property
    def state(self):
        return self._state
    
    @property
    def name(self):
        return self._name
    
    @property
    def date(self):
        return self._date
    
    def get_name(self):
        return f"{self.date}/ ({self.state})"

    
class Originater:
    def __init__(self, state, name) -> None:
        self._state = state
        self._name = name

    def change_state(self, state):
        print(f"Change state is executed.: {state}")
        self._state = state

    def change_name(self, name):
        print(f"Change name is executed.: {name}")
        self._name = name

    def __str__(self) -> str:
        return f"state: {self._state}, name: {self._name}"
    
    def save(self):
        return ConcreteMement(self._state, self._name)
    
    def restore(self, memento: ConcreteMement):
        self._state = memento.state
        self._name = memento.name
        print(f"originator: State Chene to : {self._state}")


class CareTaker:
    def __init__(self) -> None:
        self._mementos = []

    def backup(self, memento: Memento):
        print(f"save original state.: {memento.get_name()}")
        self._mementos.append(memento)

    def undo(self):
        """一つ前に戻す"""
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        return memento
    
    def show_history(self):
        print("Change log >>")
        for memento in self._mementos:
            print(memento.get_name())


class OriginaterBackup:
    """
    Originaterクラスのインスタンスの現在の状態を
    ダンプファイルに吐き出したり、ダンプファイルから復元する
    """
    @staticmethod
    def dump_to_file(originater: Originater, file_name):
        with open(file_name, mode="wb") as f:
            pickle.dump(originater, f)

    @staticmethod
    def load_by_file(file_name):
        with open(file_name, mode="rb") as f:
            originater = pickle.load(f)
        return originater



originater = Originater("Fst state", "orginator 1")
care_taker = CareTaker()
backup_instace = originater.save()
care_taker.backup(backup_instace)

originater.change_name("new name")
originater.change_state("Second state")
backup_instace = originater.save()
care_taker.backup(backup_instace)

care_taker.show_history()


print("=====================================")
originater.change_state("Third state")
originater.change_name("new new name")
print(f"** Current state is {originater}")

undo_instance = care_taker.undo()
originater.restore(undo_instance)
print(originater)

print("=====================================")
OriginaterBackup.dump_to_file(originater, "tmp.dump")

originater2 = OriginaterBackup.load_by_file("tmp.dump")
print(originater2)





