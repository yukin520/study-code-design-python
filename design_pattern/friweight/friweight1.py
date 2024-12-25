


class User:
    def __init__(self, name = "", age = "") -> None:
        self._age = age
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}"
    
# FriweightFactory
class UserFactory:
    _instances = {}

    @classmethod
    def get_instance(cls, id):
        # userクラスをキャッシュすることができる
        if id not in cls._instances:
            user = User()
            cls._instances[id] = user
            return user
        return   cls._instances.get(id)
 

user1 = UserFactory.get_instance(1)
user2 = UserFactory.get_instance(2)
user3 = UserFactory.get_instance(1)

if id(user1) == id(user3):
    print("user1 and user3 is equal")
