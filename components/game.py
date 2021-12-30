from typing import Iterable

from restrictions.restriction import Restriction


class Game:
    def __init__(self, rules: Iterable[Restriction]):
        self.rules: Iterable[Restriction] = rules

    def check(self, board: Iterable[int]) -> bool:
        for rule in self.rules:
            restricted_cells = [board[index] for index in rule.indexes]
            for check in rule.checks:
                if not check(restricted_cells):
                    return False
        return True
