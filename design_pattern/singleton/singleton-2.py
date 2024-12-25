

'''
このような書き方もあるよの例
'''
class DataBase:

    _instance  = None

    def __init__(self) -> None:
        '''
        コンストラクタは使えないようにせず、
        下のクラスメソッドからインスタンスを作成できるようにする。
        '''
        raise RuntimeError('このクラスのコンストラクタは呼び出せません')
    
    @classmethod
    def get_instance(cls, database_url=None):
        if cls._instance is None:
            # インスタンスを自明的に作成する
            cls._instance = cls.__new__(cls)

        if database_url != None:
            cls._instance._database_url = database_url

        return cls._instance

    @property
    def database_url(self):
        return self._database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self._database_url = database_url

    def connect():
        # コネクションを作成するなど
        pass


# これはRuntimeErrorになる
# a = DataBase()

# インスタンスメソッドを利用してインスタンスを生成する
a = DataBase.get_instance()
b = DataBase.get_instance()


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






