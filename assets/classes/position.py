from enum import Enum

class Position:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return bool(self.x is other.x and self.y is other.y)

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, factor: int):
        return Position(self.x * factor, self.y * factor)

    def __imul__(self, factor: int):
        self.x *= factor
        self.y *= factor
        return self

    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == 0:
            self.n += 1
            return self.x
        elif self.n == 1:
            self.n += 1
            return self.y
        else: raise StopIteration

    def get_relative_pos(self, other, distance: int=1):
        return self + ( other * distance )

class Direction(Enum) :
    UP = Position(0, -1)
    DOWN = Position(0, 1)
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
    UPLEFT = Position(-1, -1)
    UPRIGHT = Position(1, -1)
    DOWNLEFT = Position(-1, 1)
    DOWNRIGHT = Position(1, 1)