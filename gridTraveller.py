def gridTraveller(row, column, memo={}):
    if (row, column) in memo: return memo[(row, column)]
    if (column, row) in memo: return memo[(column, row)]
    if row == 1 or column == 1: return 1
    if row == 0 or column == 0: return 0

    memo[(row, column)] = gridTraveller(row - 1, column, memo) + gridTraveller(row, column - 1, memo)
    return memo[(row, column)]

print(gridTraveller(50, 50))