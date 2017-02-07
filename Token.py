from enum import Enum
class TokenCode(Enum):
    ID = "ID"
    ASSIGN = "ASSIGN"
    SEMICOL = "SEMICOL"
    INT = "INT"
    ADD = "ADD"
    SUB = "SUB"
    MULT = "MULT"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    PRINT = "PRINT"
    END = "END"
    ERROR = "ERROR"

class Token:
    lexeme = ""
    tCode = TokenCode.ID
    def __init__(self, lexeme, tCode):
        self.lexeme = lexeme
        self.tCode = tCode

    def __str__(self):
        return "Token({}, {})".format(self.lexeme, self.tCode)
