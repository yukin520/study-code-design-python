
from abc import ABC, abstractmethod

# product
class SetMeal:
    @property
    def main_dish(self):
        return self._main_dish
    
    @main_dish.setter
    def main_dish(self, main_dish):
        self._main_dish = main_dish

    @property
    def side_dish(self):
        return self._side_dish
    
    @side_dish.setter
    def side_dish(self, side_dish):
        self._side_dish = side_dish

    def __str__(self) -> str:
        return f"main dish is {self.main_dish}, side dish is {self.side_dish}"
    

# interface for builder
class SetMeakBuilder(ABC):
    def __init__(self) -> None:
        self._set_meal = SetMeal()

    @property
    @abstractmethod
    def product(self):
        pass

    @classmethod
    @abstractmethod
    def build_main_dish(self):
        pass

    @classmethod
    @abstractmethod
    def build_side_dish(self):
        pass

# builders
class SannmaSetBuilder(SetMeakBuilder):
    def __init__(self) -> None:
        super().__init__()

    @property
    def product(self):
        return self._set_meal
    
    def build_main_dish(self):
        self._set_meal.main_dish = "Sanma"
        return self

    def build_side_dish(self):
        self._set_meal.side_dish = "Miso Soup"
        return self


class PastaSetBuilder(SetMeakBuilder):
    def __init__(self) -> None:
        super().__init__()

    @property
    def product(self):
        return self._set_meal
    
    def build_main_dish(self):
        self._set_meal.main_dish = "Pasta"
        return self

    def  build_side_dish(self):
        self._set_meal.side_dish = "Salada"
        return self


# dirctor
class Director:
    def __init__(self, builder:SetMeakBuilder) -> None:
        self._builder = builder

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build(self) -> SetMeakBuilder:
        self._builder.build_main_dish()
        self._builder.build_side_dish()

        return self.builder




#  ==================main=========================

sannma_builer = SannmaSetBuilder()
director = Director(sannma_builer)
director.build()
print(director.builder.product)

pasta_builder = PastaSetBuilder()
director = Director(pasta_builder)
director.build()

print(director.builder.product)
print(director.build().product) # このような書き方もできる

