"""
Bruteforce algorithm

Check all the possible permutations of available candidates for the cells
restricted by this rule and check each one of them for complying with the rule
and given digits.

Because this is a brute force algorithm, it is slow, so please use it after you
have narrowed down the possibilities using other algorithms.
"""

import itertools

from ..util import (_complies_with_rule, _get_elements_for_rule, _has_givens,
                    _update_candidates)


def filter_candidates(game, board, candidates):
    if not game.rules:
        return candidates
    for rule in game.rules:
        cands = _get_elements_for_rule(candidates, rule.indexes)
        givens = _get_elements_for_rule(board, rule.indexes)
        perms = itertools.product(*cands)
        perms = filter(_has_givens(givens), perms)
        perms = filter(_complies_with_rule(rule), perms)
        perms = list(_flatten_permutation(perms))

        candidates = _update_candidates(candidates, perms, rule.indexes)
    return candidates


def _flatten_permutation(perms):
    for cell_cands in zip(*perms):
        yield list(set(cell_cands))
