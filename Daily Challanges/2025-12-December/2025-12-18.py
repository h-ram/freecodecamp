def print_board(board):
    for row in board:
        print(row)
    print()

def create_board(dimensions):
    grid = []

    for row in range(dimensions[0]):
        tmp = ["O"] * dimensions[1]
        for col in range(dimensions[1]):
            if row % 2 == 0 and col % 2 == 0:
                tmp[col]= 'X'
            if row % 2 == 1 and col % 2 == 1:
                tmp[col]= 'X'
        grid.append(tmp)

    print_board(grid)

    return grid


test1 = create_board([3, 3])
test2 = create_board([6, 1])
test3 = create_board([2, 10])
test4 = create_board([5, 4])


check1 = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
check2 = [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]
check3 = [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]
check4 = [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")