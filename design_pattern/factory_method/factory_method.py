

from abc import ABC, abstractmethod


class IFactory(ABC):
    def __init__(self) -> None:
        self.registerd_owners = []

    def create(self, owner):
        self._owner = owner
        prodcut = self._create_product()
        self._register_product(prodcut)

        return prodcut
    
    @classmethod
    @abstractmethod
    def _create_product(self):
        pass
    
    @classmethod
    @abstractmethod
    def _register_product(self, product):
        pass


class CarFactory(IFactory):
    def _create_product(self):
        return Car(self._owner)
    
    def _register_product(self, product):
        self.registerd_owners.append(product.owner)


class ShipFactory(IFactory):
    def _create_product(self):
        return Ship(self._owner)
    
    def _register_product(self, product):
        self.registerd_owners.append(product.owner)



class IProduct(ABC):
    def __init__(self, owner) -> None:
        self._owner = owner
    
    @classmethod
    @abstractmethod
    def use(self):
        pass

    @property
    @abstractmethod
    def owner(self):
        return self._owner
    

class Car(IProduct):
    def use(self):
        print(f"used by {self.owner}.")
    
    @property
    def owner(self):
        return self._owner
    

class Ship(IProduct):
    def use(self):
        print(f"lets got to sea with {self.owner}.")
    
    @property
    def owner(self):
        return self._owner
    

car_favtory = CarFactory()
yamada_car = car_favtory.create('yamada')
sato_car = car_favtory.create('sato')

yamada_car.use()
sato_car.use()


ship_favtory = ShipFactory()
yamada_ship = ship_favtory.create('yamada')
sato_ship =  ship_favtory.create('sato')

yamada_ship.use()
sato_ship.use()
