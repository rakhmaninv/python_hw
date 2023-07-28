from .board_generator import generate_board as gb


__all__ = ['get_valid_boards', 'queen_check']


def queen_check(board: list | tuple) -> bool:
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i][0] == board[j][0] or \
                    board[i][1] == board[j][1] or \
                    abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False
    return True


def get_valid_boards(num_of_boards: int) -> list:
    tries = []
    count = 0
    board_comb = []
    while len(board_comb) < num_of_boards:
        board = gb()
        if queen_check(board):
            tries.append(count)
            board_comb.append(board)
        count += 1
    print(tries)
    return board_comb
