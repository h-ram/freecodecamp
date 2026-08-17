def solve_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    target = max(row_sums)

    r = c = -1
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                r, c = i, j

    value = target - row_sums[r]

    if value <= 0:
        return "impossible"

    grid[r][c] = value

    target = sum(grid[0])

    for i in range(3):
        if sum(grid[i]) != target:
            return "impossible"

    for j in range(3):
        if grid[0][j] + grid[1][j] + grid[2][j] != target:
            return "impossible"

    if grid[0][0] + grid[1][1] + grid[2][2] != target:
        return "impossible"

    if grid[0][2] + grid[1][1] + grid[2][0] != target:
        return "impossible"

    return value


print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))
print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))