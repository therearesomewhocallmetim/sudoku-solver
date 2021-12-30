from ..util import _get_elements_for_rule


def filter_candidates(game, givens, candidates):
    for rule in game.rules:
        givens_for_rule = frozenset(_get_elements_for_rule(givens, rule.indexes))
        for index in rule.indexes:
            candidates[index] = list(frozenset(candidates[index]) - givens_for_rule)
    return candidates
