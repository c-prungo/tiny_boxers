from typing import List, Dict, Tuple
from enum import Enum

Tile = Dict[str, str]
Matrix = List[List[Tile]]
Position = Tuple[int, int]

class Direction(Enum) :
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)