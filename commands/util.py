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
