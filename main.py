import copy

from rich.console import Console

from rich.table import Table

import yaml

from components.game import Game
from components.strategy_loader import load_strategies, load_restrictions
from util import load_board, apply_cands_to_board


def generate_table(board) -> Table:
    """Make a new table."""
    table = Table(show_header=False, show_lines=True)
    row_values = []
    for i, cell in enumerate(board):
        values = make_cell_value(cell, i)
        row_values.append(values)
        if len(row_values) == 9:
            table.add_row(*row_values)
            row_values = []
    return table


def make_cell_value(cell, cell_number):
    background = " on white" if get_colour_for_box(cell_number) else ""
    if cell[0]:
        return f"[green{background}]   \n {cell[0]} \n   "
    nums = [str(n) if n in cell[1] else " " for n in range(1, 10)]
    return f'[black{background}]{"".join(nums[0:3])}\n{"".join(nums[3:6])}\n{"".join(nums[6:])}'


def get_colour_for_box(cell_number):
    row, col = divmod(cell_number, 9)
    row_sq = row // 3
    col_sq = col // 3
    grey = not bool((row_sq + col_sq) % 2)
    return grey


def display_board(board, candidates):
    display_board = [
        [x, y] for x, y in zip(board, candidates)
    ]
    table = generate_table(display_board)
    console.print(table)
    input("continue?")


if __name__ == "__main__":

    all_strategies = load_strategies()
    with open('config.yaml') as stream:
        config = yaml.safe_load(stream)
    print(config)

    restrictions = load_restrictions(*config['game']['rules'])
    rs = []
    for f in restrictions:
        print(f.__name__)
        rs.extend(f())
    print("RS: ")
    print(rs)
    for thing in rs:
        print(type(thing.indexes))
    game = Game(rs)
    board = load_board('board.txt')
    print(board)

    # print(all_strategies, config['game']['strategies'])


    strategies_by_name = {
        s[0]: s for s in all_strategies
    }

    strategies = [strategies_by_name[name] for name in config['game']['strategies']]
    #
    #
    # strategies = list(filter(
    #     lambda x: x[0] in config['game']['strategies'],
    #     all_strategies
    # ))

    print(strategies)


    # game = Game(restrictions)
    candidates = [list(range(1, 10))] * 81
    console = Console()


    for strategy in strategies:
        print(f"applying strategy {strategy[0]}")
        while True:
            old_cands = copy.deepcopy(candidates)
            candidates = strategy[3](game, board, candidates)

            display_board(board, candidates)
            if old_cands == candidates:
                break
            else:
                print(old_cands, '\n\n', candidates)

            board = apply_cands_to_board(board, candidates)
            display_board(board, candidates)
            input("Continue?")







    print("Imported the following strategies:")
    for i, (_, name, doc, _) in enumerate(strategies, start=1):
        print(f"{i}) {name}\n{doc}\n")

