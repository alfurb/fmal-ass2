from Token import Token, TokenCode
import sys

class Lexer:
    inp = ""
    pos = 0
    def __init__(self):
        self.inp = sys.stdin.read()

    def nextToken(self):
        next_c = self.inp[self.pos]

        while next_c.isspace():
            self.pos += 1
            next_c = self.inp[self.pos]

        if next_c.isalpha():
            return self._process_id()
        elif next_c.isdigit():
            return self._process_int()
        elif next_c == "+":
            ret = Token(next_c, TokenCode.ADD)
        elif next_c == "-":
            ret = Token(next_c, TokenCode.SUB)
        elif next_c == "(":
            ret = Token(next_c, TokenCode.LPAREN)
        elif next_c == ")":
            ret = Token(next_c, TokenCode.RPAREN)
        elif next_c == "*":
            ret = Token(next_c, TokenCode.MULT)
        elif next_c == ";":
            ret = Token(next_c, TokenCode.SEMICOL)
        elif next_c == "=":
            ret = Token(next_c, TokenCode.ASSIGN)
        else:
            ret = Token("", TokenCode.ERROR)
        self.pos += 1
        return ret

    def _process_id(self):
        ret = [self.inp[self.pos]]
        self.pos += 1
        next_c = self.inp[self.pos]
        while self.pos < len(self.inp) and next_c.isalpha():
            ret.append(next_c)
            self.pos += 1
            next_c = self.inp[self.pos]
        s = "".join(ret)
        if s == "print":
            return Token(s, TokenCode.PRINT)
        if s == "end":
            return Token(s, TokenCode.END)
        return Token(s, TokenCode.ID)

    def _process_int(self):
        ret = [self.inp[self.pos]]
        self.pos += 1
        next_c = self.inp[self.pos]
        while self.pos < len(self.inp) and next_c.isdigit():
            ret.append(next_c)
            self.pos += 1
            next_c = self.inp[self.pos]
        s = "".join(ret)
        return Token(s, TokenCode.INT)
