


"""
開放原理の原則を守った例
"""


from abc import ABCMeta, abstractmethod

class userInfo:
    def __init__(self, age, name, job_name, nationality) -> None:
        self.name = name
        self.age= age
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.job_name}, {self.nationality}"


class Comparation(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def is_equal(self, other):
        pass


class JobNameComparation(Comparation):
    def __init__(self, job_name) -> None:
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name
    
    
class NationarlityComparation(Comparation):
    def __init__(self, nationality) -> None:
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class Filter(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def fileter(self, comparation,items):
        pass


class UserInfoFileter(Filter):
    def filter(self, comparation,items):
        for item in items:
            if comparation.is_equal(item):
                yield item

taro = userInfo(name="taro", job_name="salary_man", nationality="japan")
jiro = userInfo(name="jiro", job_name="police_man", nationality="japan")
john = userInfo(name="john", job_name="salary_man", nationality="usa")

user_list = [taro, jiro, john]
user_info_fileter = UserInfoFileter

sraly_man_comparation = JobNameComparation('salary_man')
for user in user_info_fileter.filter(comparation=user_info_fileter, items= user_list):
    print(user)

japan_comparation = NationarlityComparation('japan')
for user in user_info_fileter.filter(comparation=japan_comparation, items= user_list):
    print(user)

# 機能を拡張したい場合も、Fileterクラスを継承したクラスと、専用のフィルター処理を下に書いてあげることで
# 既存のコードを変更せずに簡単に拡張可能 



# ============================================

# """
# 開放原理の原則を守っていない例
# """

# class userInfo:
#     def __init__(self, age, name, job_name, nationality) -> None:
#         self.name = name
#         self.age= age
#         self.job_name = job_name
#         self.nationality = nationality

#     def __str__(self) -> str:
#         return f"{self.name}, {self.age}, {self.job_name}, {self.nationality}"
    

# class UserInfoFileter:
#     @staticmethod
#     def filter_user_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user

#     @staticmethod
#     def filter_user_nationality(users, nationality_name):
#         for user in users:
#             if user.nationality == nationality_name:
#                 yield user
    


# taro = userInfo(name="taro", job_name="salary_man", nationality="japan")
# jiro = userInfo(name="jiro", job_name="police_man", nationality="japan")
# john = userInfo(name="john", job_name="salary_man", nationality="usa")

# user_list = [taro, jiro, john]

# for man in UserInfoFileter.filter_user_job(user_list, "salary_man"):
#     print(man)

# for man in UserInfoFileter.filter_user_nationality(user_list, "japan"):
#     print(man)


