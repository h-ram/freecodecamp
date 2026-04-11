def rook_attack(rook1, rook2):
    col1, row1 = rook1
    col2, row2 = rook2
    return col1 == col2 or row1 == row2


print(rook_attack("A1", "A8"))
print(rook_attack("B4", "F4"))
print(rook_attack("E3", "D4"))
