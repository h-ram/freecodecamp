def find_pawn_moves(position):
    moves = []
    col = position[0]
    row = position[1]

    # reached the end
    if row == '8':
        return moves

    moves.append(f"{col}{int(row)+1}")

    # first move (2 possible)
    if row == '2':
        moves.append(col + '4');

    print(position, moves)
    return moves


test1 = find_pawn_moves("D4")
test2 = find_pawn_moves("B2")
test3 = find_pawn_moves("A7")
test4 = find_pawn_moves("G2")
test5 = find_pawn_moves("E3")

check1 = ["D5"]
check2 = ["B3", "B4"]
check3 = ["A8"]
check4 = ["G3", "G4"]
check5 = ["E4"]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")