import logging
import logging.config

from classes.board import Board
from utils.typing_utils import Direction

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(board_str=r'4f1w|1w4f|3f2w|5f')
    print(board)
    board.add_boxer((2,1))
    board.add_boxer((0,1))
    board.add_boxer((3,3))
    print(board)
    board.move_boxer(0, Direction.UP, Direction.LEFT, Direction.LEFT, Direction.LEFT)
    print(board)

if __name__ == "__main__":
    main()