def navigate_trail(map_data):
    path = ""
    m = len(map_data)
    n = len(map_data[0])
    
    grid = [list(row) for row in map_data]
    
    starting_coords = [0, 0]
    found = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'C':
                starting_coords = [i, j]
                found = True
                break
        if found:
            break

    coords = list(starting_coords)
    while True:
        x, y = coords
        grid[x][y] = 'V'

        if x > 0 and (grid[x - 1][y] == 'T' or grid[x - 1][y] == 'G'):
            coords = [x - 1, y]
            path += 'U'
        elif y < n - 1 and (grid[x][y + 1] == 'T' or grid[x][y + 1] == 'G'):
            coords = [x, y + 1]
            path += 'R'
        elif x < m - 1 and (grid[x + 1][y] == 'T' or grid[x + 1][y] == 'G'):
            coords = [x + 1, y]
            path += 'D'
        elif y > 0 and (grid[x][y - 1] == 'T' or grid[x][y - 1] == 'G'):
            coords = [x, y - 1]
            path += 'L'
        else:
            break

        if grid[coords[0]][coords[1]] == 'G':
            break
            
    return path

test1 = navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])
test2 = navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"])
test3 = navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"])
test4 = navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"])
test5 = navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"])

check1 = "RDDRDD"
check2 = "RRUUURR"
check3 = "DLDDRRRRD"
check4 = "RRRDDL"
check5 = "ULLLUUURRRRRRDDDR"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")