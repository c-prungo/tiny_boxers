from ast import DictComp
from classes.position import Direction

class Action():

    def __init__(self, idx: int, type: str, dir: Direction=None):

        self.idx = idx
        self.type = type
        self.dir = dir

    def __str__(self) -> str:
        return f'boxer: {self.idx}, type: {self.type}, {self.dir}'