# NOTE: External imports
from json import load
from typing import List
from getpass import getpass

# NOTE: Full external imports
import logging

# NOTE: Custom imports
from classes.position import Position, Direction, get_legal_dirs
from classes.action import Action

with open('assets/data/actions.json') as json_file:
    actions = load(json_file)

class Boxer:

    base_actions: int = 2

    def __init__(self, pos: Position):
        self.pos = pos
        self.max_hp: int = 12
        self.hp: int = self.max_hp
        self.defense: int = 0

        self.actions = self.base_actions
        self.temp_actions: int = 0

    # overridden to compare positions
    def __eq__(self, other) -> bool:
        return self.pos is other.pos

    def get_actions(self, idx: int) -> List[Action]:
        """crude user input until UI developed"""
        print(idx)
        player_actions = []
        for _ in range(self.actions):

            action_list = [key for key in actions]
            print('\n'.join([f'{i}: {key}' for i, key in enumerate(actions)]))
            action_idx = getpass("What type of action?")
            action_type = action_list[int(action_idx)]

            action_direction = None
            if 'directions' in actions[action_type]:
                legal_dirs = actions[action_type]['directions']
                direction_list = get_legal_dirs(legal_dirs)
                print('\n'.join([f'{i}: {key}' for i, key in enumerate(direction_list)]))
                direction_idx = getpass("What direction?")
                action_direction = direction_list[int(direction_idx)]
            player_actions.append(Action(idx, action_type, action_direction))
        return player_actions

    def get_relative_pos(self, dir: Direction, distance: int=1) -> Position:
        """returns a position from the current position"""
        return self.pos.get_relative_pos(dir.value, distance)

    def move(self, pos: Position):
        """changes position to given position"""
        self.pos = pos

    def damage(self, damage: int=1, ignorecounter: bool=False):
        """deal damage to the boxer"""
        self.hp -= max( 0, (damage - ( 0 if ignorecounter else self.defense ) ) )

    def heal(self, healing: int=1):
        """increase the hp of the boxer to a maximum"""
        self.hp = min( self.max_hp, (self.hp + healing) )

    def block(self, block: int=1, extra_action: int=0):
        """block damage from any attack that hits the boxer this round"""
        self.defense = block
        self.temp_actions += extra_action
    
    def round_reset(self):
        """simple function to reset boxer after every round"""
        self.defense = 0

    def full_reset(self):
        """simple function to reset boxer after every round"""
        self.actions = self.base_actions + self.temp_actions
        self.temp_actions = 0