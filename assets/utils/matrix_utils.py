from typing import List

Matrix = List[List[str]]

def get_height(matrix: Matrix) -> int:
    return len(matrix)

def get_width(matrix: Matrix) -> int:
    return max([len(row) for row in matrix])

def banner(func):

    def inner(*args, **kwargs):

        string = func(*args, **kwargs)
        lines = string.splitlines()

        new_string = '\n'.join([f'| {l} |' for l in lines])
        banner = '|' + '~'*(len(lines[0])+2) + '|'
        return '\n'.join([
            banner,
            new_string,
            banner
        ])

    return inner