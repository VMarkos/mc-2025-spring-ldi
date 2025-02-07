# Token.py

from enum import Enum

class TokenType(Enum):
    # single character tokens
    LEFT_PAREN = 0
    RIGHT_PAREN = 1
    # add more here

    # < 3 character tokens
    BANG = 10 # you might want to change this value
    EQUAL = 11 # this too
    BANG_EQUAL = 12 # this too
    # add more here

    # EOF
    EOF = 100 # you might want to change this too

class Token:
    def __init__(
            self,
            type: TokenType,
            lexeme: str,
            literal: object,
            line: int
        ) -> None:
        self.type: TokenType = type
        self.lexeme: str = lexeme
        self.literal: object = literal,
        self.line: int = line

    def __str__(self) -> str:
        pass
        # implement a way to print tokens
        # this will also be utilised to print errors!
