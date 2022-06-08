import logging

logger = logging.getLogger('boxer')

class boxer:

    def __init__(self, name):
        logger.info('boxer created')
        self.name = name

    def __str__(self):
        return f'{self.name}'