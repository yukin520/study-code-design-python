

from abc import ABC, abstractmethod
from copy import deepcopy


class ProtoType(ABC):
    @classmethod
    @abstractmethod
    def use(self, msg):
        pass

    @classmethod
    @abstractmethod
    def _clone(self):
        pass

class MesssageBox(ProtoType):
    def __init__(self, decoration_char) -> None:
        self._decoration_char = decoration_char

    def use(self,msg):
        str_msg = str(msg)
        print(self._decoration_char * (len(str_msg) + 4))
        print(f"{self._decoration_char} {str_msg} {self.decoration_char}")
        print(self._decoration_char * (len(str_msg) + 4))


    def _clone(self):
        print('Create clopne of Message Box.')
        return deepcopy(self)
    
    @property
    def decoration_char(self):
        return self._decoration_char

    @decoration_char.setter
    def decoration_char(self, decoration_char):
        self._decoration_char = decoration_char



class UnderlinePen(ProtoType):
    def __init__(self, underline_char) -> None:
        self._underline_char = underline_char

    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)

        print(self._underline_char * (len(str_msg)))

    def _clone(self):
        print('Create clopne of Underline Pen.')
        return deepcopy(self)

    @property
    def underline_char(self):
        return self._underline_char
    
    @underline_char.setter
    def underline_char(self, underline_char):
        self._underline_char = underline_char


class Manager:
    def __init__(self) -> None:
        self._products = {}

    def register(self, name, prototype: ProtoType):
        self._products[name] = deepcopy(prototype)

    def create_product(self, name):
        product  = self._products.get(name)
        return product._clone()


#  ProtoTypeを使ってみる
m_box = MesssageBox("**")
m_box.use("hello world!")
u_pen = UnderlinePen("=")
u_pen.use("hello world!")

#  Managerから使ってみる
manager = Manager()
manager.register("msg_box", m_box)
manager.register("underline_pen", u_pen)

cloned_m_box = manager.create_product("msg_box")
cloned_m_box.use("cloned!!!")

cloned_m_box2 = manager.create_product("msg_box")
cloned_m_box2.use("hello")

cloned_u_pen = manager.create_product("underline_pen")
cloned_u_pen.use("new pen!!")










