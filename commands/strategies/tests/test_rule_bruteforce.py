from components.game import Game
from restrictions.normal_sudoku import unique
from restrictions.restriction import Restriction

from ..rule_bruteforce import filter_candidates


def test_filter_candidates():
    board = [1] + [0] * 80
    candidates = [list(range(1, 4))] * 81

    def check(l):
        return list(l) == sorted(l)

    rule = Restriction(
        indexes=[0, 1, 2],
        checks=[check, unique]
    )

    g = Game([rule])
    filtered = filter_candidates(g, board, candidates)

    assert filtered[:3] == [[1], [2], [3]]
