def row_indexes(n):
    start = n * 9
    return list(range(start, start + 9))


def column_indexes(n):
    return [x * 9 + n for x in range(9)]


def apply_cands_to_board(board, candidates):
    for i, cands in enumerate(candidates):
        if len(cands) == 1:
            if board[i]:
                raise RuntimeError(f"Board value: {board[i]}, {i = }, {cands[0] = }")
            board[i] = cands[0]
            candidates[i] = []
    return board, candidates


def load_board(filename):
    with open(filename) as infile:
        return get_board_from_str(infile.read())

def get_board_from_str(str_board):
    str_board = str_board.strip()
    str_board = str_board.replace('\n', '')
    return [int(s) for s in str_board]
