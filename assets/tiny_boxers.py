import logging
import logging.config

from classes.board import Board

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(board_str='4o1xn1x4on3o2xn5on')
    print(board)

if __name__ == "__main__":
    main()