
from abc import ABC, abstractmethod
from enum import Enum
from random import randint

"""
じゃんけんで出す手を戦略に応じて変更する実装例
"""

class HandType(Enum):
    GUU = 0
    CHOKI = 1
    PAA = 2


class Hand:
    def __init__(self, hand_index) -> None:
        if hand_index not in [0,1,2]:
            raise Exception("hand_index is incrrect.")
        self.hand_index = hand_index

    def is_win(self, other):
        if any((
            (self.hand_index == HandType.GUU.value and other.hand_index == HandType.CHOKI.value),
            (self.hand_index == HandType.CHOKI.value and other.hand_index == HandType.PAA.value),
            (self.hand_index == HandType.PAA.value and other.hand_index == HandType.GUU.value)
        )):
            return True
        return False
    
    def is_lose(self, other):
        if any((
            (self.hand_index == HandType.GUU.value and other.hand_index == HandType.PAA.value),
            (self.hand_index == HandType.CHOKI.value and other.hand_index == HandType.GUU.value),
            (self.hand_index == HandType.PAA.value and other.hand_index == HandType.CHOKI.value)
        )):
            return True
        return False
    

# strategy
class Strategy(ABC):
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, is_win):
        pass


# concrete strategy
class SimpleStrategy(Strategy):
    """勝利した場合は次も同じ手を出す戦略"""
    def __init__(self) -> None:
        self.hand = None
        self.is_win = False

    def next_hand(self):
        if not self.is_win:
            self.hand = Hand(randint(0, 2)) # GUU or CHOKI or PAA by random
        return self.hand
    
    def study(self, is_win):
        self.is_win = is_win


class ComplexStrategy(Strategy):
    """前回出した手から次に出す手のうち、最も勝利した手を出す戦略"""
    def __init__(self) -> None:
        self.current_hand = None
        self.previous_hand = None
        self.histories = [[0,0,0], [0,0,0],[0,0,0]] # var[今回の手][次の手]

    def next_hand(self):
        if self.current_hand:
            self.previous_hand = self.current_hand
        self.current_hand = self._get_most_winning_hand()
        return self.current_hand
    
    def _get_most_winning_hand(self):
        if not self.previous_hand:
            return Hand(randint(0,2))
        tmp_hand = 0
        if self.histories[self.previous_hand.hand_index][1] > self.histories[self.previous_hand.hand_index][tmp_hand]:
            tmp_hand = 1
        if self.histories[self.previous_hand.hand_index][2] > self.histories[self.previous_hand.hand_index][tmp_hand]:
            tmp_hand = 2
        return Hand(tmp_hand)

    def study(self, is_win):
        if not self.previous_hand:
            return
        if is_win:
            self.histories[self.previous_hand.hand_index][self.current_hand.hand_index] += 1
        else:
            self.histories[self.previous_hand.hand_index][(self.current_hand.hand_index + 1) % 3] += 1
            self.histories[self.previous_hand.hand_index][(self.current_hand.hand_index + 2) % 3] += 1


# context
class Player:
    def __init__(self, name, stratgy: Strategy) -> None:
        self.name = name
        self.strategy = stratgy
        self.win_count = 0
        self.lose_count = 0
        self.game_count = 0

    def next_hand(self) -> Hand:
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)  
        self.win_count += 1
        self.game_count += 1

    def lose(self):
        self.strategy.study(False)  
        self.lose_count += 1
        self.game_count += 1

    def even(self):
        self.game_count += 1
    
    def __str__(self):
        return f"{self.name}: {self.game_count} games, {self.win_count} win, {self.lose_count} lose."


taro = Player("taro", SimpleStrategy())
jiro = Player("jiro", ComplexStrategy())

for _ in range(10000):
    taro_hand = taro.next_hand()
    jiro_hand = jiro.next_hand()

    if taro_hand.is_win(jiro_hand):
        taro.win()
        jiro.lose()
    elif taro_hand.is_lose(jiro_hand):
        taro.lose()
        jiro.win()
    else:
        taro.even()
        jiro.even()

print(taro)
print(jiro)

    



