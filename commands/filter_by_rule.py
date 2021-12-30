from .util import _get_elements_for_rule, _update_candidates


def filter_candidates(game, board, candidates):
    if not game.rules:
        return candidates
    for rule in game.rules:
        cands = _get_elements_for_rule(candidates, rule.indexes)
        givens = _get_elements_for_rule(board, rule.indexes)
        if hasattr(rule, "filter_candidates"):
            candidates = _update_candidates(
                candidates,
                rule.filter_candidates(givens, cands),
                rule.indexes
            )
    return candidates
