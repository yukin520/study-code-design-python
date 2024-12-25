
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    gendor: str

# handler
class Handler(ABC):
    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler
    
    def handle(self, user: User):
        # filterがtureのとき、つまりフィルターに引っかかった場合は終了する
        if self.filter(user):
            return self.done(user)
        
        # nextが存在する場合は、次のHnadlerを実行
        if self._next:
            return self._next.handle(user)
        
        # nextが存在しない場合は、そのまま終了
        return self.end(user)

    @abstractmethod
    def filter(user: User):
        pass

    def done(self, user: User):
        print(f"{user}は{self.__class__.__name__}でフィルタリングされました。")
        return False

    def end(self, user: User):
        print(f"{user}の確認は完了しました")
        return True


# Concrete Handkers
class NameCheckhandkler(Handler):
    def filter(self, user: User):
        if user.name in ['', None, ' ', 'Nanashi']:
            return True
        return False
    
    # フィルター引っかかり終了した際のエラーメッセージをカスタマイズ
    def done(self, user: User):
        print(f"{user}の名前は空ではいけません。")
        return False


class AgeCheckHandker(Handler):
    def filter(self, user: User):
        if (user.age < 0) or (user.age > 100):
              return True
        return False
    
    def done(self, user: User):
        print(f"{user}の年齢は0以上、100以下でなければいけません。")
        return False


class GenderCheckHandker(Handler):
    def filter(self, user: User):
        if user.gendor not in ["Men", "Women"]:
            return True
        return False

    def done(self, user: User):
        print(f"{user}の性別はMenかWomenのどちらかでなければいけません")
        return False

# 利用する
name_handler = NameCheckhandkler()
age_handler = AgeCheckHandker()
gender_handler = GenderCheckHandker()

# nameのチェック、ageのチェック、genderのチェックを登録し、順番に実行する
name_handler.set_next(age_handler).set_next(gender_handler)

user = User("taro", 15, "Men")
name_handler.handle(user)


user1 = User("taro", 15, "M")
user2 = User("", 15, "Men")
user3 = User("taro", 10000, "Men")
user4 = User("taro", -15, "Men")
user5 = User("taro", 12, "Men") # こいつだけ正しく設定されているユーザー

valid_users = []
correct_users = []
for u in [user1, user2, user3, user4,  user5]:
    if name_handler.handle(u) == False:
        valid_users.append(u)
    else:
        correct_users.append(u)

print(f"valid users >> {valid_users}")
print(f"correct users >> {correct_users}")

