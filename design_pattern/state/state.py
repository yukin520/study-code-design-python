
from abc import ABC, abstractmethod
from datetime import datetime


# State
class State(ABC):
    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def end(self):
        pass


# ConcreteState
class DayState(State):
    def begin(self):
        print("start day move")

    def write_log(self):
        with open("tmp.txt", mode="w", encoding="utf-8") as f:
            f.write("log at day.")

    def end(self):
        print("finih day move")


class NightState(State):
    def begin(self):
        print("start night move")
        
    def write_log(self):
        with open("tmp.txt", mode="w", encoding="utf-8") as f:
            f.write("log at night.")

    def end(self):
        print("finih night move")
        

# Context
class Context:
    def __init__(self) -> None:
        self._state = self.change_state_by_time()

    def do(self):
        self._state.begin()
        self._state.write_log()
        self._state.end()
    
    def change_state(self, state: State):
        self._state = state

    def change_state_by_time(self):
        now = datetime.now()
        if (now.hour < 6) or (now.hour >= 19):
            self._state = NightState()
        else:
            self._state = DayState()


context = Context()
context.change_state(DayState())
context.do()

context.change_state_by_time()
context.do()
