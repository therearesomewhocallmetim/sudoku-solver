from components.game import Game
from restrictions.normal_sudoku import NormalSudoku, OneToNine

str_board = """
000090000
000403500
003200080
070020006
890500042
060301900
000700005
085104030
000030000
"""

def get_board_from_str(str_board):
    str_board = str_board.strip()
    str_board = str_board.replace('\n', '')
    return [int(s) for s in str_board]


def main():
    game = Game([
        NormalSudoku.rows(),
        NormalSudoku.columns(),
        NormalSudoku.boxes(),
        OneToNine()])

    board = get_board_from_str(str_board)
    candidates = [list(range(9))] * 81




if __name__ == "__main__":
    main()