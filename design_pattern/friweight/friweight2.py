
class FryweightMixin:
    _instances = {}

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            # クラスのインスタンスを作成して、(cls, *args)をキーにして保管
            new_insance = cls(**kwargs)
            cls._instances[(cls, *args)] = new_insance
            return new_insance
        else:
            return cls._instances.get((cls, *args))


class User(FryweightMixin):
    def __init__(self, name ,age) -> None:
        self._age = age
        self._name = name


class Car(FryweightMixin):
    def __init__(self, brand, model) -> None:
        self._brand = brand
        self._model = model

    
user1 = User.get_instance(1, name="taro", age="21")
user2 = User.get_instance(1)
print(id(user1), id(user2))

car = Car.get_instance(2, brand = "toyota", model="prius")
print(car._model)