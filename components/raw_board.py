"""
A module for a board with certain values: either "given" or computed by
processors in our programme
"""
from util import column_indexes


def get_row(row, board):
    if row < 0 or row > 8:
        raise IndexError(row)
    start = row * 9
    return board[start:start + 9]


def get_column(col, board):
    indexes = column_indexes(col)
    return [board[index] for index in indexes]


def rows(board):
    for row in range(9):
        yield get_row(row, board)


def columns(board):
    for col in range(9):
        yield get_column(col, board)


def get_box(n, board):
    b_row, b_col = divmod(n, 3)
    board_row, board_col = b_row * 3, b_col * 3
    for row in range(board_row, board_row + 3):
        for col in range(board_col, board_col + 3):
            i = row * 9 + col
            yield board[i]


def boxes(board):
    for i in range(9):
        return list(get_box(i, board))
