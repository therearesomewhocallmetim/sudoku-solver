from restrictions.restriction import Restriction

from ..util import _complies_with_rule, _has_givens, _update_candidates


def test_has_givens():
    permutations = [
        [1, 2, 3],
        [2, 3, 1],
        [3, 2, 1],
        [1, 3, 2]
    ]
    givens = [0, 2, 1]
    expected = [[3, 2, 1]]
    actual = list(filter(_has_givens(givens), permutations))
    assert actual == expected


def test_complies_with_rule():
    permutations = [
        [1, 2, 3],  # has even
        [2, 3, 1],  # not sorted
        [3, 2, 1],  # not sorted
        [1, 3, 5],  # ok
    ]
    rule = Restriction([], [
        lambda x: x == sorted(x),
        lambda x: all((el % 2 == 1 for el in x))
    ])
    expected = [
        [1, 3, 5]
    ]
    actual = list(filter(_complies_with_rule(rule), permutations))
    assert actual == expected


def test_update_candidates():
    candidates = [1, 2, 3, 4, 5, 6]
    new_candidates = [9, 8, 7, 6]
    indexes = [1, 2, 3, 4]
    expected = [1, 9, 8, 7, 6, 6]
    actual = _update_candidates(candidates, new_candidates, indexes)
    assert actual == expected
