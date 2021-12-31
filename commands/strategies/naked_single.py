"""
If a cell has a candidate that is not possible to place into any other cell,
(that is, it is not a candidate for any other cell), it will be made the only
candidate for such cell, all other candidates for this cell will be removed.
"""


from collections import Counter
from itertools import chain

from ..util import _get_elements_for_rule


def filter_candidates(game, givens, candidates):
    for rule in game.rules:
        cands_for_rule = _get_elements_for_rule(candidates, rule.indexes)
        givens_for_rule = _get_elements_for_rule(givens, rule.indexes)
        counter = Counter(chain(*cands_for_rule, givens_for_rule))
        naked_singles = {cand for cand, count in counter.items() if count == 1}
        if naked_singles:
            for index in rule.indexes:
                if single := naked_singles.intersection(candidates[index]):
                    candidates[index] = list(single)
    return candidates
