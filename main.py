import time

from board import board

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
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




l = Live()


with Live(generate_table(), auto_refresh=False) as live:
    for i in range(1, 3):
        live.update(generate_table())
        live.refresh()
        board[0][0] = i
        time.sleep(3)
    # live.update(generate_table())