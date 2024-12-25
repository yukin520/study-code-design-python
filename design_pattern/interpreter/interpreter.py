
"""
逆ポーランド記法を解釈するような実装
"""

from abc import ABC, abstractmethod


class InterpreterException(Exception):
    pass


# context
class Context:
    def __init__(self, text: str) -> None:
        self._tokens = text.split()  # "13*" -> [1,3,*]
        self._idx = 0

    @property
    def tokens(self):
        return self._tokens
    
    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self, idx):
        self._idx = idx

    def delete_tokens(self, start, end):
        del self._tokens[start:end]


# abstract expression
class Node(ABC):
    @abstractmethod
    def parse(self , context: Context):
        pass


# noterminal expression
class ProgramNode(Node):
    def parse(self, context: Context):
        try:
            while context.idx < len(context.tokens):
                idx = context.idx
                current_token = context.tokens[idx]
                if current_token == "+":   
                    node = PlusNode()
                elif current_token == "-":
                    node = MinusNode()
                elif current_token == "*":
                    node = MultiplyNode()
                elif current_token == "/":
                    node = DevideNode()
                else:
                    context.idx += 1
                    continue
                ans = node.parse(context=context)
                context.delete_tokens(idx-2, idx+1)
                context.tokens.insert(idx -2, ans)
                context.idx = idx - 1
            if len(context.tokens) == 1:
                return context.tokens[0]
            else:
                raise InterpreterException( "想定外の計算結果")
        except Exception as e:
            raise InterpreterException("文字式が間違っています", e)


# terminal expression
class PlusNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx -2]) + int(context.tokens[idx -1])


class MinusNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx -2]) - int(context.tokens[idx -1])


class MultiplyNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx -2]) * int(context.tokens[idx -1])
    

class DevideNode(Node):
    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx -2]) // int(context.tokens[idx -1])




# client
context = Context('2 1 +')
node = ProgramNode()
print(node.parse(context=context))

context = Context('2 1 + 3 + 10 * 3 /')
print(node.parse(context=context))
