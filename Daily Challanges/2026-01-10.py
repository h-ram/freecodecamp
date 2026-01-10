def tic_tac_toe(board):

    # horizontal
    if board[0][0] == board[0][1] == board[0][2]:
        return f"{board[0][0]} wins"
    if board[1][0] == board[1][1] == board[1][2]:
        return f"{board[1][0]} wins"
    if board[2][0] == board[2][1] == board[2][2]:
        return f"{board[2][0]} wins"

    # vertical
    if board[0][0] == board[1][0] == board[2][0] :
        return f"{board[0][0]} wins"
    if board[0][1] == board[1][1] == board[2][1]:
        return f"{board[0][1]} wins"
    if board[0][2] == board[1][2] == board[2][2]:
        return f"{board[0][2]} wins"

    # diagnoal
    if board[0][0] == board[1][1] == board[2][2] :
        return f"{board[0][0]} wins"
    if board[0][2] == board[1][1] == board[2][0]:
        return f"{board[1][1]} wins"
    
    return "Draw"

    

test1 = tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]) 
test2 = tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]])
test3 = tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])
test4 = tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]])
test5 = tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]])
test6 = tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]])

check1 = "X wins"
check2 = "O wins"
check3 = "Draw"
check4 = "O wins"
check5 = "X wins"
check6 = "Draw"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")