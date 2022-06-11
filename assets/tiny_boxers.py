import logging
import logging.config

from classes.board import Board
from utils.typing_utils import Direction

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(board_str=r'3f|3f|3f')
    print(board)
    board.add_boxer((1,0))
    board.add_boxer((1,2))
    print(board)
    board.move_boxer(0, Direction.UP, Direction.LEFT, Direction.LEFT, Direction.LEFT)
    print(board)

if __name__ == "__main__":
    main()