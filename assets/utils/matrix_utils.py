from typing import List

Matrix = List[List[str]]

def get_height(matrix: Matrix) -> int:
    return len(matrix)

def get_width(matrix: Matrix) -> int:
    return max([len(row) for row in matrix])