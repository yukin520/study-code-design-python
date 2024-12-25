
from abc import ABC, abstractmethod


class Component(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass
    
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def print_list(self, path):
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.size})"


class File(Component):
    def __init__(self, name, size) -> None:
        self._name = name
        self._size = size
        self._parent = None

    @property
    def name(self):
        return self._name
    
    @property
    def size(self):
        return self._size

    def print_list(self, path=''):
        print(path + "/" + str(self))
    

class Directory(Component):
    def __init__(self, name) -> None:
        self._name = name
        self._children = {}   #  ファイル or ディレクトリのdict
        self._parent = None

    @property
    def name(self):
        return self._name
    
    @property
    def size(self):
        file_size = 0
        for child in self._children:
            file_size += self._children[child].size
        return file_size
    
    def add_child(self, child: Component):
        self._children[child.name] = child
        child.parent = self

    def remove_child(self, child: Component):
        if child.name in self._children:
            del self._children[child.name]
            child.parent = None

    def print_list(self, path=""):
        print(path + "/" + str(self))

        for child in self._children:
            self._children[child].print_list(path + "/" + self.name)
    


file1 = File("tmp1.txt", 1000)
file2 = File("tmp2.txt", 2000)
file3 = File("tmp3.txt", 3000)
file4 = File("tmp4.txt", 4000)

root_dir = Directory("root")
home_dir = Directory("home")
sys_dir = Directory("sys")
taro_dir = Directory("taro")

root_dir.add_child(home_dir)
root_dir.add_child(sys_dir)

home_dir.add_child(taro_dir)

taro_dir.add_child(file1)
taro_dir.add_child(file2)

home_dir.add_child(file3)
sys_dir.add_child(file4)

root_dir.print_list()

print("+++++++++++++++++++++")
root_dir.remove_child(home_dir)
root_dir.print_list()

