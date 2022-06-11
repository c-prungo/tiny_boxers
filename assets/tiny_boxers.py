import logging
import logging.config

from classes.board import Board
from classes.position import Position, Direction

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(board_str=''.join(3*'3f|'))
    # board = Board(r'3f|3f|3f')
    print(board)
    board.add_boxer(Position(1, 0), Position(1, 2))
    print(board)
    board.move_boxer(0, Direction.UP, Direction.LEFT, Direction.LEFT, Direction.LEFT)
    print(board)

if __name__ == "__main__":
    main()