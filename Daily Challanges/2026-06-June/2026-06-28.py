def connect_three(board):
    if not board or not board[0]:
        return []

    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "":
                continue
            for dr, dc in directions:
                cells = []
                for k in range(3):
                    nr = r + dr * k
                    nc = c + dc * k
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    if board[nr][nc] != board[r][c]:
                        break
                    cells.append([nr, nc])
                if len(cells) == 3:
                    cells.sort()
                    return [board[r][c]] + cells
    return []

print(connect_three([
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "Y", "", ""],
    ["Y", "R", "R", "R"]
]))

print(connect_three([
    ["", "", "", ""],
    ["", "Y", "Y", ""],
    ["", "Y", "R", "R"],
    ["", "Y", "R", "R"]
]))

print(connect_three([
    ["", "", "Y", "R"],
    ["", "Y", "R", "Y"],
    ["", "R", "Y", "R"],
    ["", "R", "Y", "R"]
]))

print(connect_three([
    ["", "Y", "", ""],
    ["", "Y", "Y", ""],
    ["", "R", "R", "Y"],
    ["R", "R", "Y", "R"]
]))

print(connect_three([
    ["Y", "R", "R", "Y"],
    ["R", "Y", "Y", "R"],
    ["Y", "R", "R", "Y"],
    ["R", "Y", "Y", "R"]
]))