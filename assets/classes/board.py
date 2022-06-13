# NOTE: External imports
from typing import List
from json import load
from copy import deepcopy
from pprint import pprint

# NOTE: Full external imports
import logging

# NOTE: Custom imports
from classes.matrix import BoardMatrix
from classes.boxer import Boxer
from classes.position import Position, Direction
from classes.action import Action

logger = logging.Logger('boxer', level=logging.DEBUG)

with open('assets/data/actions.json') as json_file:
    actions = load(json_file)

class Board:

    # Dunder
    def __init__(self, board_str: str):

        self.board = BoardMatrix(board_str)
        self.boxers: List[Boxer] = []

    def __str__(self):

        grid = self.board.get_literal()

        for i, boxer in enumerate(self.boxers):
            grid[boxer.pos] = str(i)

        return '\n'.join(
            [str(grid),
            *[f'  {i}: {str(boxer.hp)}' for i, boxer in enumerate(self.boxers)]]
        )

    # Core
    def add_boxer(self, *positions: Position):
        """add a new boxer to the board, fails if the position is taken"""

        for pos in positions:

            new_boxer = Boxer(pos)

            # check if boxers share a position
            for boxer in self.boxers:
                if boxer == new_boxer: return

            if self.is_legal_pos(pos):
                self.boxers.append(new_boxer)

    def take_actions(self, *player_actions: Action):

        # order is important as it determines order of resolution
        type_list = [
            "move",
            "block",
            "attack"
        ]

        for type_str in type_list:

            stage = []
            for action in player_actions:
                if actions[action.type]["type"] == type_str: stage.append(action)

            check = True
            new_board = deepcopy(self)
            for action in stage:
                if new_board.take_action(type_str, **vars(action)) == False: check = False

            if check == True:
                self.boxers = new_board.boxers

    def take_action(self, key: str, idx: int, type: str, dir: Direction) -> bool:

        type_dict = {
            "move": self.move_boxer,
            "block": self.boxer_block,
            "attack": self.boxer_attack
        }

        try:
            action = deepcopy(actions[type])

            del action['type']

            if not all(self.check_directions(dir, directions=action['directions'])): return False
            del action['directions']

            return type_dict[key](idx, dir, **action)

        except Exception as e:
            logger.exception(str(e))
            return False

    # Minor
    def move_boxer(self, idx: int, dir: Direction, distance: int=1) -> bool:
        """move a boxer in a single direction with a given range (only makes legal moves)"""

        new_pos = self.boxers[idx].get_relative_pos(dir, distance)
        if self.is_legal_pos(new_pos):
            self.boxers[idx].move(new_pos)
            return True

        return False

    def boxer_block() -> bool:
        return True

    def boxer_attack(self, idx: int, dir: Direction, damage: int, distance: int) -> bool:

        new_pos = self.boxers[idx].get_relative_pos(dir, distance)
        for boxer in self.boxers:
            if boxer.pos == new_pos: boxer.damage(damage)

        return True

    # Helper
    def check_directions(self, *dirs: Direction, directions: List[int]) -> bool:
        """check if a list of directions are legal directions"""

        parsed_directions = []
        for direction in directions:
            if direction == "straight":
                parsed_directions.extend([0,1,2,3])
            if direction == "diagonal": parsed_directions.extend([4,5,6,7])
            if type(direction) == int: parsed_directions.append(direction)

        valid_dirs = []
        for i, dir_enum in enumerate(Direction):
            if i in parsed_directions: valid_dirs.append(dir_enum)

        results = []
        for dir in dirs:
            results.append(bool(dir in valid_dirs))
        return results

    def is_legal_pos(self, pos: Position) -> bool:
        """check if a position exists on the board"""
        if (self.is_within_board(pos)
        and self.is_tile(pos, 'f')
        and self.is_free_tile(pos)): return True
        return False

    def is_within_board(self, pos: Position) -> bool:
        """check if a position exists within the bounds of the board"""

        # guard: check that the position exists in the matrix
        try: self.board[pos]
        except Exception as e:
            logger.exception('Failed is_within_board guard check: ' + str(e))
            return False

        # check the position isn't negative
        return bool(pos.x >= 0 and pos.y >= 0)

    def is_tile(self, pos: Position, *tiles: str) -> bool:
        """check if the floor tile at a given position is within a certain set of tiles"""
        try:
            return bool(self.board[pos]['tile'] in tiles)
        except Exception as e:
            logger.exception('Failed is_tile check: ' + str(e))
            return False

    def is_free_tile(self, pos: Position) -> bool:
        """check if a given position contains another boxer"""
        try:
            return False if not all([boxer.pos != pos for boxer in self.boxers]) else True
        except Exception as e:
            logger.exception('Failed is_free_tile check: ' + str(e))
            return False