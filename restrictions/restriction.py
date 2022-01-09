from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass
class Restriction:
    indexes: Iterable[int]
    checks: Iterable[Callable[[Iterable[int]], bool]]
