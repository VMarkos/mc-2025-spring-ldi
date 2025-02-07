# Scanner.py

from Token import Token

class Scanner:
    def __init__(self, source: str) -> None:
        self.source: str = source
        self.tokens: list[Token] = []

    def scan_tokens(self) -> list[Token]:
        return []