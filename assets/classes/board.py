# NOTE: External imports
from json import load
from re import split
from typing import List

# NOTE: Full imports
import logging

# NOTE: Custom imports
from classes.boxer import Boxer
from utils.typing_utils import Matrix, Position, Direction

logger = logging.Logger('boxer', level=logging.DEBUG)

with open('assets/data/tiles.json') as json_file:
    tiles = load(json_file)

class Board:

    def __init__(self, board_str: str):

        self.board = bsn_to_board(board_str)
        self.boxers: List[Boxer] = []

    def __str__(self):

        matrix = [ [ str(m['tile']) for m in row ] for row in self.board ]
        for i, boxer in enumerate(self.boxers):
            matrix[boxer.y()][boxer.x()] = str(i)

        board = '\n'.join(
            [ f"| {'  '.join([ m for m in row ])} |" for row in matrix ]
        )

        banner = '|' + '~'*((len(self.board[0])*3)) + '|'
        return '\n'.join([
            banner,
            board,
            banner
        ])

    def add_boxer(self, pos: Position):
        """add a new boxer to the board, fails if the position is taken"""
        new_boxer = Boxer(pos=pos)
        for boxer in self.boxers:
            if boxer == new_boxer: return
        if self.is_legal_pos(pos): self.boxers.append(new_boxer)

    def is_boxer(self, idx: int) -> bool:
        return bool(0 <= idx < len(self.boxers))

    def move_boxer(self, idx: int, *dirs: Direction):
        if not self.is_boxer(idx): return
        for dir in dirs:
            new_pos = self.boxers[idx].get_move(dir)
            if self.is_legal_pos(new_pos): self.boxers[idx].move(new_pos)

    def is_legal_pos(self, pos: Position) -> bool:
        return bool(self.board[pos[1]][pos[0]]['tile'] == "f")

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
    return matrix