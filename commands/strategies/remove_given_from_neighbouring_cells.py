"""
Any number that is a given (either by the puzzle setters or found during solving,
this number can no longer be a candidate for other cells in this row, column
or box (or the cell indexes specified by the rule). Such given digits shall
be removed from such candidates.
"""


from ..util import _get_elements_for_rule


def filter_candidates(game, givens, candidates):
    for rule in game.rules:
        givens_for_rule = frozenset(_get_elements_for_rule(givens, rule.indexes))
        for index in rule.indexes:
            candidates[index] = list(frozenset(candidates[index]) - givens_for_rule)
    return candidates
