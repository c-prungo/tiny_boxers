import logging
import logging.config

from classes.boxer import boxer
from classes.directions import Directions
from utils.cli_ui import display_board

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    width, height = 3, 3
    board_size = width * height
    dir = Directions(width)
    boxer_1 = boxer(id=1, position=2, board_size=board_size)
    boxer_2 = boxer(id=2, position=8, board_size=board_size)

    display_board(width=width, height=height, boxers=[boxer_1, boxer_2])
    boxer_1.move(dir.move(width=width, height=height, position=boxer_1.position, directions=['up', 'right']))
    print("-"*100)
    display_board(width=width, height=height, boxers=[boxer_1, boxer_2])
    boxer_1.move(dir.move(width=width, height=height, position=boxer_1.position, directions=['down']))
    print("-"*100)
    display_board(width=width, height=height, boxers=[boxer_1, boxer_2])
    boxer_1.move(dir.move(width=width, height=height, position=boxer_1.position, directions=['down', 'left', 'left']))
    print("-"*100)
    display_board(width=width, height=height, boxers=[boxer_1, boxer_2])

if __name__ == "__main__":
    main()