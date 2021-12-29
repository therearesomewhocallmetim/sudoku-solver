import pytest

from components.raw_board import rows, columns, get_box


def test_rows():
    b = list(range(81))
    for i, row in enumerate(rows(b)):
        assert row == list(range(start := i * 9, start + 9))


def test_cols():
    b = list(range(81))
    for i, col in enumerate(columns(b)):
        expected = [x * 9 + i for x in range(9)]
        assert col == expected


@pytest.mark.parametrize("n, expected", [
    (0, [0, 1, 2, 9, 10, 11, 18, 19, 20]),
    (4, [30, 31, 32, 39, 40, 41, 48, 49, 50]),
    (8, [60, 61, 62, 69, 70, 71, 78, 79, 80]),
])
def test_get_box(n, expected):
    b = list(range(81))
    assert list(get_box(n, b)) == expected




