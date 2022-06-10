from typing import List

from utils.bsn_utils import bsn_to_matrix
from utils.matrix_utils import get_height, get_width

class Board:

    def __init__(self, board_str: str):

        self.matrix = bsn_to_matrix(board_str)
        self.height = get_height(self.matrix)
        self.width = get_width(self.matrix)
        self.direction_dict = {
            "up": -self.width,
            "down": self.width,
            "left": -1,
            "right": 1,
        }

    def __str__(self):

        return '\n'.join(
            [ '  '.join(
                [str(m) for m in row]
            ) for row in self.matrix ]
        )