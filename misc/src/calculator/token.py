

class Token:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        raise NotImplementedError


class NumberToken(Token):
    def get_value(self) -> int:
        return self._value


class VariableToken(Token):
    def get_value(self) -> str:
        return self._value


class CommandToken(Token):
    def get_value(self) -> str:
        return self._value




class Parser:
    def process(self, line: str) -> [Token]:
        pass
