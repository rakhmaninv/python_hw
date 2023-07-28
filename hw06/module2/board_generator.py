from random import randint

__all__ = ['generate_board']

BOARDS = []


def _add_board(board: list):
    BOARDS.append(board)


def generate_board() -> tuple:
    num_of_queens = 6
    board_length = 8
    while True:
        new_board = []
        while len(new_board) < num_of_queens:
            coord = (randint(1, board_length), randint(1, board_length))
            if coord not in new_board:
                new_board.append(coord)
        if new_board not in BOARDS:
            _add_board(new_board)
            return tuple(new_board)
