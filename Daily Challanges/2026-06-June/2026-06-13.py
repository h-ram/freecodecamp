def get_zone_violations(grid):
    violations = []
    if not grid or not grid[0]:
        return violations

    rows, cols = len(grid), len(grid[0])
    invalid_adj = {
        "i": {"R", "I"},
        "A": {"C"},
        "R": {"i", "C"},
        "I": {"i"},
        "C": {"R", "A"},
        "": set(),
    }

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            is_violating = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor = grid[nr][nc]
                    if neighbor in invalid_adj.get(cell, set()):
                        is_violating = True
                        break
            if is_violating:
                violations.append([r, c])

    return violations


print(get_zone_violations([["R", "C"], ["", "C"]]))
print(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]))
print(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]))
print(
    get_zone_violations(
        [["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]
    )
)
print(
    get_zone_violations(
        [
            ["R", "A", "A", "", "i", "i"],
            ["R", "I", "", "C", "i", "i"],
            ["R", "", "C", "C", "A", "A"],
            ["R", "R", "C", "I", "R", "R"],
        ]
    )
)
