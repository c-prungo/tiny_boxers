import logging

logger = logging.getLogger('boxer')

class Boxer:

    def __init__(self, id: int, position: int, board_size: int):
        self.id = id
        self.position = position
        self.board_size = board_size

    def __str__(self) -> str:
        return f'{str(self.id)}'

    def __add__(self, movement: float):
        new_position = self.position + movement
        if self.board_size >= new_position > 0: self.position = new_position

    def __sub__(self, movement: float):
        new_position = self.position - movement
        if self.board_size >= new_position > 0: self.position = new_position

    def move(self, new_pos: int):
        if self.board_size >= new_pos > 0: self.position = new_pos