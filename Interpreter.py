import fileinput
import re

class Interpreter :
    def __init__(self):
        self.stack = []
        self.identifiers = dict()

        self.int_regex = re.compile(r"[-+]?\d+$")

    def is_int(self, x):
        return self.int_regex.match(str(x)) is not None

    def get_ident_value(self, ident):
        if type(ident) == int:
            return ident
        elif ident in self.identifiers:
            return self.identifiers[ident]
        else:
            raise ValueError

    def pop(self):
        if len(self.stack) == 0:
            raise ValueError
        return self.stack.pop()

    def pop_two(self):
        return (self.pop(), self.pop())

    def push(self, x):
        if self.is_int(x):
            self.stack.append(int(x))
        else:
            self.stack.append(x)

    def print(self):
        x = self.pop()
        x = self.get_ident_value(x)
        print(x)

    def add(self):
        x, y = self.pop_two()
        x = self.get_ident_value(x)
        y = self.get_ident_value(y)
        self.push(x + y)

    def sub(self):
        x, y = self.pop_two()
        x = self.get_ident_value(x)
        y = self.get_ident_value(y)
        self.push(y - x)

    def mult(self):
        x, y = self.pop_two()
        x = self.get_ident_value(x)
        y = self.get_ident_value(y)
        self.push(x * y)

    def assign(self):
        x, y = self.pop_two()
        x = self.get_ident_value(x)
        if self.is_int(y):
            raise ValueError
        self.identifiers[y] = x

    def execute(self):
        for line in fileinput.input():
            try:
                line = line.split()
                if line[0] == "PUSH":
                    self.push(line[1])
                elif line[0] == "ADD":
                    self.add()
                elif line[0] == "SUB":
                    self.sub()
                elif line[0] == "MULT":
                    self.mult()
                elif line[0] == "ASSIGN":
                    self.assign()
                elif line[0] == "PRINT":
                    self.print()
                else:
                    raise ValueError
            except ValueError:
                print("Error for operator", line[0])
                exit(1)


if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.execute()
