
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ShowCharComponent(Component):
    def __init__(self, char) -> None:
        self._char = char

    def operation(self):
        print(self._char * 20)


class ShowDecorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component


class ShowMessage(ShowDecorator):
    def __init__(self, component: Component, msg: str) -> None:
        super().__init__(component)
        self._msg = msg

    def operation(self):
        """
        デコレーターの実装
        """
        self._component.operation()  # Componentのメソッド
        print(self._msg) # ShowMessageクラスのメソッド
        self._component.operation()


class WriteDecorator(Component):
    def __init__(self, component: Component, filename: str, msg: str) -> None:
        self._component = component
        self._msg = msg
        self._filemame = filename


class WriteMessage(WriteDecorator):
    def operation(self):
        """
        デコレーターの実装
        """
        self._component.operation()
        with open(file=self._filemame, mode="w") as f:
            f.write(self._msg)



show_component = ShowCharComponent("-")
# show_component.operation()

show_message = ShowMessage(show_component, "HelloWorld!!")
# show_message.operation()


write_messge = WriteMessage(show_message, "tmp.txt", "write_message")
write_messge.operation()