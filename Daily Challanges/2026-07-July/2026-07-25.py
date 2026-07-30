def find_signal(grid):
    rows = len(grid)
    cols = len(grid[0])
    towers = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                towers.append((r, c, grid[r][c]))

    for r in range(rows):
        for c in range(cols):
            valid = True

            for tr, tc, d in towers:
                if max(abs(r - tr), abs(c - tc)) != d:
                    valid = False
                    break

            if valid:
                return [r, c]


print(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
print(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]))
print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))
print(find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]))