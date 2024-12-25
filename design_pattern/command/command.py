
from abc import ABC, abstractmethod
from enum import Enum


class CommandNummber(Enum):
    LIGHT = 0
    TV = 1
    GAME  = 2


# Reciever
class TV:
    def __init__(self, name) -> None:
        self._name = name

    def on_tv(self):
        print(f"TV: {self._name}を ONにします")

    def off_tv(self):
        print(f"TV: {self._name}を OFFにします")


class Light:
    def __init__(self, name) -> None:
        self._name = name
    
    def on_light(self):
        print(f"ライト: {self._name}をONにします")

    def off_light(self):
        print(f"ライト: {self._name}をOFFにします")


class Game:
    def __init__(self, name) -> None:
        self._name = name

    def on_game(self):
        print(f"ゲーム: {self._name}をONにします")

    def off_game(self):
        print(f"ゲーム: {self._name}をOFFにします")


# Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 

    @abstractmethod
    def undo(self):
        pass


class NoCommnad(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommnad(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self):
        self._light.on_light()

    def undo(self):
        self._light.off_light()


class LightOffCommnad(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self):
        self._light.off_light()

    def undo(self):
        self._light.on_light()


class TVOnCommnad(Command):
    def __init__(self, tv: TV) -> None:
        self._tv = tv

    def execute(self):
        self._tv.on_tv()

    def undo(self):
        self._tv.off_tv()


class TVOffCommnad(Command):
    def __init__(self, tv: TV) -> None:
        self._tv = tv

    def execute(self):
        self._tv.off_tv()

    def undo(self):
        self._tv.on_tv()


class GameOnCommnad(Command):
    def __init__(self, game: Game) -> None:
        self._game = game

    def execute(self):
        self._game.on_game()

    def undo(self):
        self._game.off_game()


class GameOffCommnad(Command):
    def __init__(self, game: Game) -> None:
        self._game = game

    def execute(self):
        self._game.off_game()

    def undo(self):
        self._game.on_game()


# Invoker
class RemoteController:
    def __init__(self) -> None:
        self._on_commands = [NoCommnad] * len(CommandNummber)
        self._off_commands = [NoCommnad] * len(CommandNummber)
        self._undo_commands = [NoCommnad] * len(CommandNummber)

    def set_command(self, number, on_command: Command, off_command: Command):
        self._on_commands[number] = on_command
        self._off_commands[number] = off_command

    def on_command(self, number):
        self._on_commands[number].execute()
        self._undo_commands[number] = self._on_commands[number]

    def off_command(self, number):
        self._off_commands[number].execute()
        self._undo_commands[number] = self._off_commands[number]

    def undo_command(self, number):
        self._undo_commands[number].undo()



light = Light("My Light")
tv = TV("REGZA")
game = Game("Nintendo")

light_on_command = LightOnCommnad(light=light)
light_off_command = LightOffCommnad(light=light)

tv_on_command = TVOnCommnad(tv=tv)
tv_off_command = TVOffCommnad(tv=tv)

game_on_command = GameOnCommnad(game=game)
game_off_command = GameOffCommnad(game=game)

remote_controller = RemoteController()
remote_controller.set_command(CommandNummber.LIGHT.value,light_on_command, light_off_command)
remote_controller.set_command(CommandNummber.TV.value, tv_on_command, tv_off_command)
remote_controller.set_command(CommandNummber.GAME.value, game_on_command, game_off_command)


# execute command
remote_controller.on_command(number=CommandNummber.LIGHT.value)
remote_controller.off_command(number=CommandNummber.LIGHT.value)
remote_controller.on_command(number=CommandNummber.TV.value)
remote_controller.off_command(number=CommandNummber.TV.value)
remote_controller.on_command(number=CommandNummber.GAME.value)
remote_controller.off_command(number=CommandNummber.GAME.value)
remote_controller.undo_command(number=CommandNummber.GAME.value)




