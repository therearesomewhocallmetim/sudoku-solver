def row_indexes(n):
    start = n * 9
    return list(range(start, start + 9))

def column_indexes(n):
    return [x * 9 + n for x in range(9)]

