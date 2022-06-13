import logging
import logging.config

from classes.board import Board
from classes.position import Position, Direction
from classes.action import Action

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    board = Board(''.join(3*'3f|'))
    # board = Board(r'3f|3f|3f')
    board.add_boxer(Position(1, 1), Position(1, 2))
    print(board)
    while True: run_round(board)

def run_round(board: Board):

    actions = board.get_actions()
    for round in actions:
        for action in round:
            print(action)
        board.take_actions(*round)

    board.full_reset()

    print(board)

if __name__ == "__main__":
    main()