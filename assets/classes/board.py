# NOTE: External imports
from json import load
from re import split
from typing import List
from pprint import pprint

# NOTE: Full imports
import logging

# NOTE: Custom imports
from classes.boxer import Boxer
from utils.typing_utils import Matrix, Position, Direction
from utils.matrix_utils import banner

logger = logging.Logger('boxer', level=logging.DEBUG)

with open('assets/data/tiles.json') as json_file:
    tiles = load(json_file)

class Board:

    def __init__(self, board_str: str):

        self.board = bsn_to_board(board_str)
        self.boxers: List[Boxer] = []

    @banner # not necessary, adds border to string
    def __str__(self):

        matrix = [ [ str(m['tile']) for m in row ] for row in self.board ]
        for i, boxer in enumerate(self.boxers):
            matrix[boxer.y()][boxer.x()] = str(i)

        return '\n'.join(
            [ '  '.join([ m for m in row ]) for row in matrix ]
        )

    def add_boxer(self, pos: Position):
        """add a new boxer to the board, fails if the position is taken"""

        new_boxer = Boxer(pos=pos)

        # check if boxers share a position
        for boxer in self.boxers:
            if boxer == new_boxer: return

        if self.is_legal_pos(pos): self.boxers.append(new_boxer)

    def is_boxer(self, idx: int) -> bool:
        """check if a given id is a valid boxer"""
        return bool(0 <= idx < len(self.boxers))

    def move_boxer(self, idx: int, *dirs: Direction):
        """move a boxer in a given set of directions (only makes legal moves)"""

        # guard check
        if not self.is_boxer(idx): return

        for dir in dirs:
            new_pos = self.boxers[idx].get_move(dir)
            if self.is_legal_pos(new_pos):
                self.boxers[idx].move(new_pos)

    def is_legal_pos(self, pos: Position) -> bool:
        """check if a position exists on the board"""

        try:
            return bool(
                pos[0] >= 0 and pos[1] >= 0
                and self.board[pos[1]][pos[0]]['tile'] == "f"
            )
        except Exception:
            return False

def bsn_to_board(board_str: str) -> Matrix:
    """convert from board string notation (bsn) to a usable board matrix"""
    num_string = "1234567890"

    try:
        parts = split(r'(\d+)', board_str)[1::]
    except Exception:
        logger.exception('Failed to parse board string...')
        raise

    matrix = []
    row = []
    num = 1
    for part in parts:

        # isolated event:
        if part[0] in num_string:
            num = max(num, int(part))
            continue
        # split -> only ints or str
        # can safely continue

        end = False
        tile_dict = {
            'tile': None
        }
        for l in part:
            if l == '|': end = True
            if l in tiles: tile_dict['tile'] = l
        row.extend([tile_dict for _ in range(num)])
        num = 1
        
        if end:
            matrix.append(row)
            row = []
    matrix.append(row)

    width = max(*[len(row) for row in matrix])

    tile_dict = {
        'tile': 'w'
    }
    for i, row in enumerate(matrix):
        diff = width-len(row)
        matrix[i].extend([tile_dict for _ in range(diff)])

    return matrix