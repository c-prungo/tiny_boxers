from typing import List

from classes.boxer import boxer

def display_board(width: int, height: int, boxers: List[boxer]):

    matrix = [0 for _ in range(width * height)]
    for player in boxers:
        matrix[player.position-1] = player
    
    display_matrix = []
    row = []
    for i, element in enumerate(matrix):
        row.append(str(element))
        if i % width == 2:
            display_matrix.append('  '.join(row))
            row = []

    print('\n'.join(display_matrix))