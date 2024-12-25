

from abc import ABC

class Knife(ABC):
    def __init__(self,name) -> None:
        self._name = name

    def cut_vegitable(self):
        print(f"野菜を{self._name}でカットします")


class Boiler:
    def __init__(self, name) -> None:
        self._name = name

    def boil_vegetables(self):
        print(f"野菜を{self._name}でカットします")

class Frier:
    def __init__(self, name) -> None:
        self._name = name

    def fry_vegetabeles(self):
        print(f"野菜を{self._name}でフライにします")

# Facade
class Cook:
    def __init__(self, knife: Knife, frier: Frier, boiler: Boiler)  -> None:
        self._knife = knife
        self._frier = frier
        self._boiler = boiler

    def cook_dish(self):
        self._knife.cut_vegitable()
        self._frier.fry_vegetabeles()
        self._boiler.boil_vegetables()


knife = Knife("My knife")
frier = Frier("My Frier")
boiler = Boiler("My Boiler")

# # Facadeパターンを使用しない例
# knife.cu_vegitable()
# boiler.boil_vegetables()
# frier.fry_vegetabeles()


# Facadeパターンを使用した例
cook = Cook(knife=knife, frier=frier, boiler=boiler)
cook.cook_dish()

