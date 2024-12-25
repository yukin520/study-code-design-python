

from abc import ABC, abstractmethod

class AbcItem(ABC):
    def __init__(self,caption) -> None:
        self.caption = caption

    @classmethod
    @abstractmethod
    def make_html(self):
        pass


class PageItem(AbcItem):
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.content =  []

    def add(self, item):
        self.content.append(item)

    def write_html(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.make_html())

    def make_html(self):
        pass


class LinkItem(AbcItem):
    # create a a tag item (<li><a></a>) 
    def __init__(self, caption, url) -> None:
        super().__init__(caption)
        self.url = url


class ListItem(AbcItem):
    # create a lsit item (<li></li>) 
    def __init__(self, caption) -> None:
        super().__init__(caption)
        self.items = []

    def add(self, item):
        self.items.append(item)


class Factory(ABC):
    @classmethod
    @abstractmethod
    def creata_page_item(self, title , author) -> PageItem:
        pass

    @classmethod
    @abstractmethod
    def create_link_item(self, caption, url) -> LinkItem:
        pass
    
    @classmethod
    @abstractmethod
    def create_list_item(self, caption) -> ListItem:
        pass
    