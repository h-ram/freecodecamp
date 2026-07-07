def bucket_fill(grid, start, new_value):
    rows = len(grid)
    cols = len(grid[0])
    row, col = start
    old_value = grid[row][col]

    if old_value == new_value:
        return grid

    stack = [(row, col)]

    while stack:
        r, c = stack.pop()

        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        if grid[r][c] != old_value:
            continue

        grid[r][c] = new_value

        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

    return grid


print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))
print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
print(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"))
print(
    bucket_fill(
        [
            ["T", "T", "R", "T"],
            ["R", "T", "R", "T"],
            ["R", "T", "R", "T"],
            ["T", "T", "T", "T"],
        ],
        [0, 3],
        "Y",
    )
)
print(
    bucket_fill(
        [
            ["G", "B", "G", "B"],
            ["R", "B", "B", "G"],
            ["B", "G", "B", "R"],
            ["B", "G", "G", "B"],
        ],
        [2, 2],
        "G",
    )
)
