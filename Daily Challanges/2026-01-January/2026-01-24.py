def get_bingo_letter(n):
    if n < 16:
        return "B"
    if n < 31:
        return "I"
    if n < 46:
        return "N"
    if n < 61:
        return "G"
    return "O"


test1 = get_bingo_letter(75)
test2 = get_bingo_letter(54)
test3 = get_bingo_letter(25)
test4 = get_bingo_letter(38)
test5 = get_bingo_letter(11)

check1 = "O"
check2 = "G"
check3 = "I"
check4 = "N"
check5 = "B"


print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
