# NOTE: External imports
from copy import deepcopy

# NOTE: Full external imports
import logging

# NOTE: Custom imports
from classes.position import Position, Direction

class Boxer:

    def __init__(self, pos: Position):
        self.pos = pos
        self.max_hp: int = 12
        self.hp: int = self.max_hp
        self.block = 0

    # overridden to compare positions
    def __eq__(self, other) -> bool:
        return self.pos is other.pos

    def get_relative_pos(self, dir: Direction, distance: int=1) -> Position:
        """returns a position from the current position"""
        return self.pos.get_relative_pos(dir.value, distance)

    def move(self, pos: Position):
        """changes position to given position"""
        self.pos = pos

    def damage(self, damage: int=1):
        """deal damage to the boxer"""
        self.hp -= max( 0, (damage - self.block) )

    def heal(self, healing: int=1):
        """increase the hp of the boxer to a maximum"""
        self.hp = min( self.max_hp, (self.hp + healing) )

    def guard(self, block: int=1):
        """block damage from any attack that hits the boxer this round"""
        self.block = block
    
    def reset(self):
        """simple function to reset boxer after every round"""
        self.block = 0