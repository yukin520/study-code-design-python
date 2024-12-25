
class DataBase:

    _instance  = None
    def __new__(cls) :
        # クラス変数で既にインスタンス化されているかどうか確認し、
        # このクラスのインスタンスは一つだけだと保証する
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._database_url = None

    @property
    def database_url(self):
        return self._database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self._database_url = database_url

    def connect():
        # コネクションを作成するなど
        pass



a = DataBase()
b = DataBase()

# インスタンスが全く同じことを確認できる
if a == b:
    print("is eequal")
else:
    print("is uneequal")
print(f"id for a is {id(a)}, id for b is {id(b)}.")


a.database_url = "http://db.example.com:3228"
print(a.database_url)

b.database_url = "http://db-1.example.com:3228"

# 同じインスタンスを参照するので、値が変化する
print(a.database_url)






