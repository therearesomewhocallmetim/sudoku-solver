def filter_candidates(game, board, candidates):
    print(">>>>running remove_given_from_cands")
    for i, given in enumerate(board):
        if given:
            candidates[i] = []
    return candidates
