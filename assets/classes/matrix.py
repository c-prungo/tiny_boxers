# NOTE: External imports
from re import split
from json import load
from typing import overload, List

# NOTE: Full external imports
import logging

# NOTE: Custom imports
from classes.position import Position
from utils.typing_utils import Tile, Row, Grid, LiteralRow

logger = logging.Logger('boxer', level=logging.DEBUG)

with open('assets/data/tiles.json') as json_file:
    tiles = load(json_file)

class Matrix:

    def __init__(self, bsn: str):

        self.grid = bsn_to_matrix(bsn)

    @overload
    def __getitem__(self, idx: Position) -> str | Tile:
        """get the element at a given position"""
        ...

    @overload
    def __getitem__(self, idx: int) -> List[str | Tile]:
        """get the row at a given index"""
        ...

    def __getitem__(self, idx):
        
        if type(idx) == int: return self.grid[idx]

        # invert x y positions from standard notation
        if type(idx) == Position: return self.grid[idx.y][idx.x]

    @staticmethod
    def stringify(func):

        def grid_to_string(*args, **kwargs):

            grid = func(*args, **kwargs)
            return '\n'.join(['  '.join(row) for row in grid])

        return grid_to_string

class LiteralMatrix(Matrix):

    def __init__(self, grid: Grid, idx: str='tile'):

        self.grid = [ [ str(m[idx]) for m in row ] for row in grid ]

    @Matrix.stringify
    def __str__(self) -> str:
        return self.grid

    def __setitem__(self, pos: Position, value: str):

        # invert x y positions from standard notation
        self.grid[pos.y][pos.x] = value

class BoardMatrix(Matrix):

    def get_literal(self, idx: str='tile') -> LiteralMatrix:
        return LiteralMatrix(self.grid, idx)

    @Matrix.stringify
    def __str__(self, idx: str='tile'):

        return self.get_literal(self.grid, idx)

def bsn_to_matrix(bsn: str) -> Grid:
    """convert from board string notation (bsn) to a usable board matrix"""
    num_string = "1234567890"

    try:
        parts = split(r'(\d+)', bsn)[1::]
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
        # split -> only ints or str:
        # - can safely check only element 0
        # - can safely continue if True

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
    if row: matrix.append(row)

    width = max(*[len(row) for row in matrix])

    tile_dict = {
        'tile': 'w'
    }
    for i, row in enumerate(matrix):
        diff = width-len(row)
        matrix[i].extend([tile_dict for _ in range(diff)])

    return matrix