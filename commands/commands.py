import itertools


def remove_givens_from_candidates(game, board, candidates):
    if not game.rules:
        return candidates
    for rule in game.rules:
        cands = _get_elements_for_rule(candidates, rule.indexes)
        givens = _get_elements_for_rule(board, rule.indexes)
        if hasattr(rule, "remove_givens_from_candidates"):
            candidates = _update_candidates(
                candidates,
                rule.remove_givens_from_candidates(givens, cands),
                rule.indexes
            )
        else:
            perms = itertools.product(*cands)
            perms = filter(_has_givens(givens), perms)
            perms = filter(_complies_with_rule(rule), perms)
            candidates = _update_candidates(candidates, perms, rule.indexes)
    return candidates


def _get_elements_for_rule(board, indexes):
    return [board[i] for i in indexes]

def _has_givens(givens):
    def filter_fn(perm):
        for p, g in zip(perm, givens):
            if not g:
                continue
            if g != p:
                return False
        return True
    return filter_fn

def _complies_with_rule(rule):
    def filter_fn(perm):
        for check in rule.checks:
            if not check(perm):
                return False
        return True
    return filter_fn


def _update_candidates(candidates, new_candidates, indexes):
    for index, cands in zip(indexes, new_candidates):
        candidates[index] = cands
    return candidates
