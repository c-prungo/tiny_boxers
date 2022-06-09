import logging
import logging.config

from classes.boxer import boxer

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

def main():

    boxer_test = boxer("test boxer 1")

if __name__ == "__main__":
    main()