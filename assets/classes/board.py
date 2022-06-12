# NOTE: External imports
from hashlib import new
from json import load
from re import split
from typing import List
from pprint import pprint

# NOTE: Full external imports
import logging

# NOTE: Custom imports
from classes.matrix import BoardMatrix
from classes.boxer import Boxer
from classes.position import Position, Direction
from utils.matrix_utils import banner

logger = logging.Logger('boxer', level=logging.DEBUG)

class Board:

    def __init__(self, board_str: str):

        self.board = BoardMatrix(board_str)
        self.boxers: List[Boxer] = []

    @banner
    def __str__(self):

        grid = self.board.get_literal()

        for i, boxer in enumerate(self.boxers):
            grid[boxer.pos] = str(i)

        return str(grid)

    def add_boxer(self, *positions: Position):
        """add a new boxer to the board, fails if the position is taken"""

        for pos in positions:

            new_boxer = Boxer(pos)

            # check if boxers share a position
            for boxer in self.boxers:
                if boxer == new_boxer: return

            if self.is_legal_pos(pos):
                self.boxers.append(new_boxer)

    def is_boxer(self, idx: int) -> bool:
        """check if a given id is a valid boxer"""
        return bool(0 <= idx < len(self.boxers))

    def move_boxer(self, idx: int, *dirs: Direction):
        """move a boxer in a given set of directions (only makes legal moves)"""

        # guard check
        if not self.is_boxer(idx): return

        for dir in dirs:
            new_pos = self.boxers[idx].get_relative_pos(dir)
            if self.is_legal_pos(new_pos):
                self.boxers[idx].move(new_pos)

    def attack(self, pos: Position):
        for boxer in self.boxers:
            if boxer.pos == pos: boxer.damage()

    def is_legal_pos(self, pos: Position) -> bool:
        """check if a position exists on the board"""
        if (self.is_within_board(pos)
        and self.is_tile(pos, 'f')): return True
        return False

    def is_within_board(self, pos: Position) -> bool:
        """check if a position exists within the bounds of the board"""

        # guard: check that the position exists in the matrix
        try: self.board[pos]
        except Exception as e:
            logger.debug('Failed is_within_board guard check: ' + str(e))
            return False

        # check the position isn't negative
        return bool(pos.x >= 0 and pos.y >= 0)

    def is_tile(self, pos: Position, *tiles: str) -> bool:
        """check if the floor tile at a given position is within a certain set of tiles"""
        try:
            return bool(self.board[pos]['tile'] in tiles)
        except Exception as e:
            logger.debug('Failed is_tile check: ' + str(e))
            return False