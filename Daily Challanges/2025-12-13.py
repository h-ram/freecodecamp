def print_grid(grid):
    for row in grid:
        print(row)
    print("---------")

def game_of_life(grid):

    grid_copy = [row[:] for row in grid]

    n_rows = len(grid)
    n_cols = len(grid[0])

    r = n_rows - 1
    c = n_cols - 1
    for i in range(n_rows):
        for j in range(n_cols):
            count = 0
            count += i > 0 and grid[i-1][j]
            count += j < c and grid[i][j+1] 
            count += i < r and grid[i+1][j]
            count += j > 0 and grid[i][j-1]
            count += i > 0 and j < c and grid[i-1][j+1]
            count += i < r and j < c and grid[i+1][j+1]
            count += i < r and j > 0 and grid[i+1][j-1]
            count += i > 0 and j > 0 and grid[i-1][j-1]
            
            if count < 2 or count > 3:
                grid_copy[i][j] = 0
            if count == 3:
                grid_copy[i][j] = 1
    return grid_copy


test1 = game_of_life([
    [0, 1, 0],
    [0, 1, 1],
    [1, 1, 0]
])

test2 = game_of_life([
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 0]
])

test3 = game_of_life([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

test4 = game_of_life([
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 0]
])

check1 = [[0, 1, 1], [0, 0, 1], [1, 1, 1]]
check2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]]
check3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
check4 = [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")