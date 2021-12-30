import itertools

from commands.util import _get_elements_for_rule, _has_givens, _complies_with_rule, _update_candidates


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
