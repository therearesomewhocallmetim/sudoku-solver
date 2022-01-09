import copy
import pathlib

import click
import yaml
from rich.console import Console
from rich.table import Table

from components.game import Game
from components.strategy_loader import load_restrictions, load_strategies
from util import apply_cands_to_board, load_board


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
    return f'[blue{background}]{"".join(nums[0:3])}\n{"".join(nums[3:6])}\n{"".join(nums[6:])}'


def get_colour_for_box(cell_number):
    row, col = divmod(cell_number, 9)
    row_sq = row // 3
    col_sq = col // 3
    grey = not bool((row_sq + col_sq) % 2)
    return grey


def display_board(board, candidates):
    board_to_display = [
        [x, y] for x, y in zip(board, candidates)
    ]
    table = generate_table(board_to_display)
    console = Console()
    console.print(table)
    input("continue?")


def board_has_been_solved(board):
    return len(list(filter(lambda x: x > 0, board))) == 81


def apply_strategy_while_works(strategy, game, board, candidates):
    while True:
        old_cands = copy.deepcopy(candidates)
        print(strategy[1])
        candidates = strategy[3](game, board, candidates)

        if board_has_been_solved(board):
            return True
        if old_cands == candidates:
            return False

        board, candidates = apply_cands_to_board(board, candidates)
        display_board(board, candidates)


def apply_all_strategies_while_work(strategies, game, board, candidates):
    while True:
        old_cands = copy.deepcopy(candidates)
        for strategy in strategies:
            if apply_strategy_while_works(strategy, game, board, candidates):
                return True
        if old_cands == candidates:
            print("None of the strategies works any more")
            return False


@click.command(
    help='''A programme for solving sudoku puzzles.
    
    Specify the applicable rules in a yaml file, specify the board in a txt file.
    
    You can write additional restrictions by inheriting from the 
    `restrictions.restriction.Restriction` class;
    
    You can provide more strategies by adding python modules to the 
    `commands.strategies` package. Each such module must contain a
    `filter_candidates(game, givens, candidates)` function that should return the
    possible candidates after applying the strategy to the existing candidates.
    '''
)
@click.option(
    '-g', '--game-conf',
    default='config.yaml',
    type=pathlib.Path,
    help='The file describing the applicable rules')
@click.option(
    '-b', '--board',
    default='board.txt',
    type=pathlib.Path,
    help='The board. Emtpy cells are represented by zeros, givens by the corresponding digits'
)
def main(game_conf, board):
    with open(game_conf) as stream:
        config = yaml.safe_load(stream)

    strategies = load_strategies(config['game']['strategies'])
    restrictions = load_restrictions(config['game']['rules'])
    game = Game(restrictions)
    board = load_board(board)

    c = Console()
    c.rule('[bold red] Sudoku Solver ')
    c.print("[green underline]Imported the following strategies:")
    for i, (_, name, doc, _) in enumerate(strategies, start=1):
        c.print(f"[yellow]{i}) {name}[reset]\n{doc}\n")
    input("continue?")

    candidates = [list(range(1, 10))] * 81

    solved = apply_all_strategies_while_work(strategies, game, board, candidates)
    if solved:
        print("The puzzle has been solved")
    else:
        print("Failed to solve the puzzle")


if __name__ == "__main__":
    main()
