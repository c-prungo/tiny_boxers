import logging
import logging.config

from classes.board import Board
from classes.position import Position, Direction
from classes.action import Action

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(board_str=''.join(3*'3f|'))
    # board = Board(r'3f|3f|3f')
    print(board)
    board.add_boxer(Position(1, 0), Position(1, 2))
    print(board)
    board.take_actions(Action(0, 'footwork', Direction.DOWN), Action(1, 'footwork', Direction.UP))
    print(board)
    board.take_actions(Action(0, 'footwork', Direction.DOWN), Action(1, 'footwork', Direction.LEFT))
    print(board)
    board.take_actions(Action(0, 'footwork', Direction.LEFT), Action(1, 'cross', Direction.UP))
    print(board)

if __name__ == "__main__":
    main()