import pytest

from components.game import Game
from restrictions.normal_sudoku import NormalSudoku


@pytest.mark.parametrize("board, result", [
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 1, 3, 4, 5, 6], False),
    ([1, 2, 3, 4, 4, 6], False),
    ([1, 2, 3, 3, 2, 1], True),

])
def test_all_checks_apply(board, result):
    r1 = NormalSudoku([0, 1, 2])
    r2 = NormalSudoku([3, 4, 5])
    g = Game(rules=[r1, r2])

    assert g.check(board) == result
