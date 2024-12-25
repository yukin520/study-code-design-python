

"""
インターフェイス分離の原則を満たしている例。

実施質的なインターフェースであるSwimAtheleteとJumpAthelete
はそれぞれ必要最小限の抽象メソッドしか用意されていないので、
継承先クラスでは余計な関数は実装しなくて良い。

もしアスリート共通のメソッドが必要になった場合はAthleteインターフェイスに
抽象メソッドを定義することで最小限の変更で済む。
"""

from abc import ABCMeta, abstractmethod

class Athlete(metaclass=ABCMeta ):
    pass

class SwimAthelete(metaclass = Athlete):
    @classmethod
    @abstractmethod
    def swim(self):
        pass

class JumpAthelete(metaclass = Athlete):
    @classmethod
    @abstractmethod
    def high_jump(self):
        pass

    @classmethod
    @abstractmethod
    def long_jump(self):
        pass

class Swimmer(SwimAthelete):
    def swim(self):
        print("i am swimminng.")

class Jumper(JumpAthelete):
    def long_jump(self):
        print("i am long jumping.")

    def high_jump(self):
        print("i am high jumping.")


john = Swimmer()
john.swim()

kevin = Jumper()
kevin.high_jump()
kevin.long_jump()



# """
# インターフェイス分離の原則を満たしていない例。

# Athleteクラスの継承先クラスであるSwimmerで、
# high_jumpやlong_jumpなどの必要のないメソッドを
# 実装する必要が出てきてしまっている。
# """

# from abc import ABCMeta, abstractmethod

# class Athlete(metaclass=ABCMeta ):

#     @classmethod
#     @abstractmethod
#     def swim(self):
#         pass

#     @classmethod
#     @abstractmethod
#     def high_jump(self):
#         pass

#     @classmethod
#     @abstractmethod
#     def long_jump(self):
#         pass


# class Swimmer(Athlete):
#     def swim(self):
#         print("i am swimminng.")
    
#     def high_jump(self):
#         pass

#     def long_jump(self):
#         pass

# jhon = Swimmer()
# jhon.swim()

