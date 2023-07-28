from module2 import *

board = [(2, 7), (3, 6), (1, 7), (3, 1), (4, 3), (7, 6), (4, 5), (8, 4)]
print(queen_check(board))

valid_boards = get_valid_boards(4)
for board in valid_boards:
    print(board)
