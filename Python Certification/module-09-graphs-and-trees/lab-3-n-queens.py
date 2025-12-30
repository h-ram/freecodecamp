
def dfs_n_queens(n):
    result = []
    if n < 1:
        return result

    def is_safe(board, row, col):
        # check vertically
        for i in range(row):
            if board[i] == col:
                return False
        
        # check diagonaly
        for i in range(row):
            if abs(row - i) == abs(col - board[i]):
                return False
        
        return True
    
    def backtrack(board, row):
        # reached the end: return a copy of the board
        if row == n:
            result.append(board[:])
            return
        
        # try every possible next placement
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
    
    board = [-1] * n
    backtrack(board, 0)
    return result



test1 = dfs_n_queens(1)
test2 = dfs_n_queens(2)
test3 = dfs_n_queens(3)
test4 = dfs_n_queens(4)
test5 = dfs_n_queens(5)


check1 = [[0]]
check2 = []
check3 = []
check4 = [[1, 3, 0, 2], [2, 0, 3, 1]]
check5 = [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")