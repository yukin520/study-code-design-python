
from abc import ABC, abstractmethod

"""
SettigsWindowとHelpWindowは
どちらか片方しか開けない

SettigsWindowやHelpWindowが開いている際は
MainWindowも開いているようにしたい。

MainWindowを閉じる場合は
SettigsWindowやHelpWindowも閉じる
"""

# Colleague
class WindowBase(ABC):
    def __init__(self, mediator=None) -> None:
        self._mediator = mediator
        self._is_open = False

    @property
    def mediator(self):
        return self._mediator
    
    @mediator.setter
    def mediator(self,  mediator):
        self._mediator = mediator
    
    @property
    def is_open(self):
        return self._is_open
    
    @is_open.setter
    def is_open(self, is_open):
        self._is_open = is_open

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


# Concrete Colleague
class MainWindow(WindowBase):
    def open(self):
        print("Open Main Window")
        self.is_open = True

    def close(self):
        self.mediator.notify("main", "open")
        print("Close Main Window")
        self.is_open = False


class SettigsWindow(WindowBase):
    def open(self):
        self.mediator.notify("settings", "open")
        print("Open Settings Window")
        self.is_open = True

    def close(self):
        print("Close Settings Window")
        self.is_open = False


class HelpWindow(WindowBase):
    def open(self):
        self.mediator.notify("help", "open")
        print("Open Help Window")
        self.is_open = True

    def close(self):
        print("Close Help Window")
        self.is_open = False


# Mediator
class Mediator(ABC):
    @abstractmethod
    def notify(self, sendor, action):
        pass


class WindowMediator(Mediator):
    def __init__(self, 
                 main_window: MainWindow, 
                 settings_window: SettigsWindow, 
                 help_window: HelpWindow) -> None:
        self._main_window = main_window
        self._settings_window = settings_window
        self._help_window = help_window

        main_window.mediator = self
        settings_window.mediator = self
        help_window.mediator = self

    def notify(self, sendor, action):
        if sendor == "settngs":
            if action == "open" and self._help_window.is_open:
                self._help_window.close()

        if sendor == "help":
            if action == "open" and self._settings_window.is_open:
                self._settings_window.close()             

        if sendor == "main":
            if action == "close" and self._settings_window.is_open:
                self._settings_window.close()    

            if action == "close" and self._help_window.is_open:
                self._help_window.close()   


main_window = MainWindow()
settings_window = SettigsWindow()
help_window = HelpWindow()

mediator = WindowMediator(main_window=main_window, 
                          settings_window=settings_window,
                          help_window=help_window
                          )

main_window.open()
settings_window.open()
help_window.open()






