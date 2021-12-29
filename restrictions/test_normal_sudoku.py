import pytest

from restrictions.normal_sudoku import NormalSudoku, unique


@pytest.mark.parametrize("row, expected", [
    (0, [0, 1, 2, 3, 4, 5, 6, 7, 8]),
    (8, [72, 73, 74, 75, 76, 77, 78, 79, 80])
])
def test_rows(row, expected):
    rows = NormalSudoku.rows()
    assert rows[row].indexes == expected
    assert rows[row].checks == [unique]


@pytest.mark.parametrize("col, expected", [
    (0, [0, 9, 18, 27, 36,  45, 54, 63, 72]),
    (8, [8, 17, 26, 35, 44, 53, 62, 71, 80])
])
def test_columns(col, expected):
    cols = NormalSudoku.columns()
    assert cols[col].indexes == expected
    assert cols[col].checks == [unique]

@pytest.mark.parametrize("n, expected", [
    (0, [0, 1, 2, 9, 10, 11, 18, 19, 20]),
    (4, [30, 31, 32, 39, 40, 41, 48, 49, 50]),
    (8, [60, 61, 62, 69, 70, 71, 78, 79, 80]),
])
def test__get_box(n, expected):
    boxes = NormalSudoku.boxes()
    assert boxes[n].indexes == expected
    assert boxes[n].checks == [unique]



