
from abc import ABC, abstractmethod


# adaptee
class ModelAdaptee(ABC):
    @classmethod
    @abstractmethod
    def load_headers(self):
        pass

    @classmethod
    @abstractmethod
    def yield_row(self):
        pass

class UserModel(ModelAdaptee):
    def __init__(self) -> None:
        self._users = []
        self._headers = ["Name", "Age"]

    def load_headers(self):
        return self._headers
    
    def yield_row(self):
        for user in self._users:
            yield user

    @property
    def users(self):
        return self._users
    
    def add_user(self, user: list):
        self._users.append(user)


# adapter
class ModelAdapter(ABC):
    @classmethod
    @abstractmethod
    def write_to_csv(self):
        pass


class UserModelAdapter(ModelAdapter):
    def __init__(self, user_model: UserModel) -> None:
        self._user_model = user_model

    def write_to_csv(self, filename):
        with open(file=filename, mode='w', encoding="utf-8", newline='\n') as f:
            csv_header = ','.join(self._user_model.load_headers())
            f.write(csv_header + "\n")
            for row in self._user_model.yield_row():
                csv_row = ','.join([str(r) for r in row])
                f.write(csv_row + "\n")


users = UserModel()
users.add_user(["taro",18])
users.add_user(["jiro",19])
users.add_user(["kotaro",17])
print(users.load_headers())
for user in users.yield_row():
    print(user)

user_model_adapter = UserModelAdapter(user_model=users)
user_model_adapter.write_to_csv("gof.csv")
