from Lexer import Lexer
from Token import Token, TokenCode
import sys
class Parser:
    lexer = None
    token = None
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = lexer.nextToken()

    def parse(self):
        self._stmts()

    def _error(self):
        print("syntaxu erroru!")
        sys.exit()
        self.token = self.lexer.nextToken()

    def _op(self, tCode):
        if self.token.tCode == tCode:
            self.token = self.lexer.nextToken()
            return
        self._error();

    def _expr(self):
        self._term()
        if self.token.tCode == TokenCode.ADD or self.token.tCode == TokenCode.SUB:
            op = "ADD" if self.token.tCode == TokenCode.ADD else "SUB"
            self.token = self.lexer.nextToken()
            self._expr()
            print(op)
        return

    def _term(self):
        self._factor()
        if self.token.tCode == TokenCode.MULT:
            self.token = self.lexer.nextToken()
            self._term()
            print("MULT")
        return

    def _factor(self):
        if self.token.tCode == TokenCode.INT or self.token.tCode == TokenCode.ID:
            print("PUSH", self.token.lexeme)
            self.token = self.lexer.nextToken()
            return
        elif self.token.tCode == TokenCode.LPAREN:
            self.token = self.lexer.nextToken()
            self._expr()
            if self.token.tCode == TokenCode.RPAREN:
                self.token = self.lexer.nextToken()
                return
        self._error()

    def _stmt(self):
        if self.token.tCode == TokenCode.ID:
            print("PUSH", self.token.lexeme)
            self.token = self.lexer.nextToken()
            self._op(TokenCode.ASSIGN)
            self._expr()
            print("ASSIGN")
            return
        elif self.token.tCode == TokenCode.PRINT:
            self.token = self.lexer.nextToken()
            if self.token.tCode == TokenCode.ID:
                print("PUSH", self.token.lexeme)
                self.token = self.lexer.nextToken()
            else:
                self._error()
            print("PRINT")
            return

    def _stmts(self):
        if self.token.tCode == TokenCode.END:
            return
        else:
            self._stmt()
            self._op(TokenCode.SEMICOL)
            self._stmts()
            return

if __name__ == "__main__":
    sys.setrecursionlimit(25)
    p = Parser(Lexer())
    p.parse()
