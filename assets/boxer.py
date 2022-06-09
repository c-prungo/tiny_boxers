import logging

logger = logging.getLogger('boxer')

class boxer:
    name = str()

    def __init__(self, name: str):
        logger.debug(name)
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'