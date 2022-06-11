from utils.typing_utils import Position, Direction

class Boxer:

    def __init__(self, pos: Position):
        self.pos = pos

    def __str__(self) -> str:
        return f'{str(self.id)}'

    def __eq__(self, other) -> bool:
        return self.pos == other.pos

    def x(self) -> int:
        return self.pos[0]

    def y(self) -> int:
        return self.pos[1]

    def get_move(self, dir: Direction):
        """returns a new position when moved in a given direction"""
        return (
            self.pos[0] + dir.value[0],
            self.pos[1] + dir.value[1]
        )

    def move(self, pos: Position):
        self.pos = pos