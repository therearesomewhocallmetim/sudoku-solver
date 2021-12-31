"""
If the true value for a cell is known, this cell can no longer have candidates,
the candidates for such cells will be set to an empty list
"""

def filter_candidates(game, board, candidates):
    for i, given in enumerate(board):
        if given:
            candidates[i] = []
    return candidates
