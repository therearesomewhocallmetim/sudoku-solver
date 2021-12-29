from typing import Iterable

from restrictions.restriction import Restriction
from util import row_indexes, column_indexes


def unique(nums: Iterable[int]) -> bool:
    return len(set(nums)) == len(list(nums))


class NormalSudoku(Restriction):
    def __init__(self, indexes):
        super().__init__(indexes, [unique])

    @staticmethod
    def rows():
        ret = []
        for row in range(9):
            ret.append(NormalSudoku(indexes=row_indexes(row)))
        return ret

    @staticmethod
    def columns():
        ret = []
        for col in range(9):
            ret.append(NormalSudoku(indexes=column_indexes(col)))
        return ret

    @staticmethod
    def _get_box(n):
        b_row, b_col = divmod(n, 3)
        board_row, board_col = b_row * 3, b_col * 3
        for row in range(board_row, board_row + 3):
            for col in range(board_col, board_col + 3):
                i = row * 9 + col
                yield i

    @staticmethod
    def boxes():
        ret = []
        for n in range(9):
            ret.append(
                NormalSudoku(indexes=list(NormalSudoku._get_box(n))))
        return ret




