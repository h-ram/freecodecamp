def knight_moves(position):
    coords_dict = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8
    }
    x = coords_dict[position[0]]
    y = int(position[1])
    
    n_moves = 0
    
    n_moves += y < 7 and x < 8 # up-left
    n_moves += y < 7 and x > 1 # up-right
    n_moves += y > 2 and x < 8 # down-left
    n_moves += y > 2 and x > 1 # down-right
    n_moves += y < 8 and x < 7 # right-up
    n_moves += y > 1 and x < 7 # right-down
    n_moves += y < 8 and x > 2 # left-up
    n_moves += y > 1 and x > 2 # left-down

    return n_moves

# All Possible moves

# up-left
# up-right
# down-left
# down-right
# right-up
# right-down
# left-up
# left-down

test1 = knight_moves("A1")
test2 = knight_moves("D4")
test3 = knight_moves("G6")
test4 = knight_moves("B8")
test5 = knight_moves("H3")

check1 = 2
check2 = 8
check3 = 6
check4 = 3
check5 = 4

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")