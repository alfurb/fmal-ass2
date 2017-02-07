from Lexer import Lexer
from Token import Token, TokenCode

class Compiler:
    def __init__(self):
        l = Lexer()
        t = l.nextToken()
        while t.tCode != TokenCode.END:
            print(t)
            t = l.nextToken()
        print(t)

if __name__ == "__main__":
    c = Compiler()
