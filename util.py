def row_indexes(n):
    start = n * 9
    return list(range(start, start + 9))


def column_indexes(n):
    return [x * 9 + n for x in range(9)]


def apply_cands_to_board(board, candidates):
    for i, cands in enumerate(candidates):
        if len(cands) == 1:
            board[i] = cands[0]
    return board
