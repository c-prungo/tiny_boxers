from classes.position import Position, Direction

class Boxer:

    def __init__(self, pos: Position):
        self.pos = pos
        self.hp: int = 12

    # overridden to compare positions
    def __eq__(self, other) -> bool:
        return self.pos is other.pos

    def get_relative_pos(self, dir: Direction):
        """returns a position from the current position"""
        return self.pos + dir.value

    def move(self, pos: Position):
        """changes position to given position"""
        self.pos = pos

    def damage(self, damage: int=1):
        """deal damage to the boxer"""
        self.hp -= damage