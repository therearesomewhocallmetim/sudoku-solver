from typing import Iterable

from restrictions.restriction import Restriction
from util import row_indexes, column_indexes


def unique(nums: Iterable[int]) -> bool:
    nums = list(filter(bool, nums))
    return len(set(nums)) == len(list(nums))


def in_allowed_range(nums: Iterable[int]) -> bool:
    nums = list(filter(bool, nums))
    return min(nums) >= 1 and max(nums) <= 9


class OneToNine(Restriction):
    def __init__(self):
        super().__init__(list(range(81)), in_allowed_range)


class NormalSudoku(Restriction):
    def __init__(self, indexes):
        super().__init__(indexes, [unique])

    def filter_candidates(self, givens, candidates):
        new_cands = []
        givens = frozenset(givens)
        for cand in candidates:
            new_cands.append(list(frozenset(cand) - givens))
        return new_cands

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




