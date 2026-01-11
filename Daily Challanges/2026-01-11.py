
def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    elif par - strokes == 2:
        return "Eagle"
    elif par - strokes == 1:
        return "Birdie"
    elif par - strokes == 0:
        return "Par"
    elif par - strokes == -1:
        return "Bogey"
    elif par - strokes == -2:
        return "Double bogey"
    return "Unknown"

test1 = golf_score(3, 3)
test2 = golf_score(4, 3)
test3 = golf_score(3, 1)
test4 = golf_score(5, 7)
test5 = golf_score(4, 5)
test6 = golf_score(5, 3)

check1 = "Par"
check2 = "Birdie"
check3 = "Hole in one!"
check4 = "Double bogey"
check5 = "Bogey"
check6 = "Eagle"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")