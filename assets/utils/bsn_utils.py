from typing import List

def bsn_to_matrix(board_str: str) -> List[List[str]]:
    """convert from board string notation (msn) to a usable map matrix"""
    num_string = "1234567890"
    char_string = "ox"

    matrix = []
    num_str = "0"
    row = []
    for l in board_str:

        if l in num_string:
            num_str += l

        if l == 'n':
            matrix.append(row)
            row = []

        if l in char_string:
            num = int(num_str)

            if num <= 0:
                num = 1

            row = [*row, *[l for _ in range(num)]]
            num_str = "0"

    return matrix