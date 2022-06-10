from typing import Dict, List
from classes.boxer import boxer

Keyword = Dict[str, float]

class Directions:

    def __init__(self, width: int):
        self.direction_dict = {
            "up": -width,
            "down": width,
            "left": -1,
            "right": 1,
        }

    def move(self, width: int, height: int, position: int, directions: List[str]) -> int:

        def parse_direction_dict(keyword: str) -> float:

            if keyword in self.direction_dict:
                return self.direction_dict[keyword]
            else:
                raise "Direction not in direction_dict..."

        def check_position(direction: float):
            if ( width * height) >= ( position + direction ) > 0: return direction
            return 0

        def handle_vertical(direction: float) -> float:
            return check_position(direction)
            
        def handle_horizontal(direction: float) -> float:
            new_direction = direction
            if position % width == 0: new_direction = min(0, direction)
            if position % width == 1: new_direction = max(0, direction)
            return check_position(new_direction)

        new_position = position
        for keyword in directions:

            direction = parse_direction_dict(keyword)

            if keyword == "up" or keyword == "down": new_position += handle_vertical(direction)
            if keyword == "left" or keyword == "right": new_position += handle_horizontal(direction)

        return new_position
