from typing import Iterable, Callable


class Restriction:
    def __init__(self, indexes, checks):
        self.indexes: Iterable[int] = indexes
        self.checks: Iterable[Callable[[Iterable[int]], bool]] = checks
