

class userInfo:
    def __init__(self, age, name, phone_number) -> None:
        self.name = name
        self.age= age
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.phone_number}"
    
    ## 以下の関数をつけてしまうと「ユーザー情報を保持する」というuserInfoクラスの定義からはずれてしまい、
    ## 単一責任の法則を満たしていないことになる
    # def write_str_to_file(self, filename):
    #     with open(filename, mode="w") as f:
    #         f.write(str(self))


# このように別のクラスを作成することで単一責任の原則を維持する
class FileManager:
    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename , mode="w") as f:
            f.write(str(obj))


user_info  = userInfo(1, "hoge", "1111111")
FileManager.write_str_to_file(obj=user_info, filename="hoge.txt")




