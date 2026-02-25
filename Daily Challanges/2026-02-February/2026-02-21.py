def score_curling(house):
    red = []
    yellow = []

    for i in range(5):
        for j in range(5):
            if house[i][j] == 'R':
                red.append(max(abs(i-2), abs(j-2)))
            elif house[i][j] == 'Y':
                yellow.append(max(abs(i-2), abs(j-2)))

    if not red and not yellow:
        return "No points awarded"

    if not red:
        return f"Y: {len(yellow)}"
    if not yellow:
        return f"R: {len(red)}"

    closest_red = min(red)
    closest_yellow = min(yellow)

    if closest_red == closest_yellow:
        return "No points awarded"

    if closest_red < closest_yellow:
        points = sum(1 for r in red if r < closest_yellow)
        return f"R: {points}"
    else:
        points = sum(1 for r in yellow if r < closest_red)
        return f"Y: {points}"

test1 = score_curling([
    [".", ".", "R", ".", "."],
    [".", "R", ".", ".", "."],
    ["Y", ".", ".", ".", "."], 
    [".", "R", ".", ".", "."], 
    [".", ".", ".", ".", "."]
])
test2 = score_curling([
    [".", ".", "R", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", "Y", ".", "R"],
    [".", ".", "Y", "Y", "."],
    [".", "Y", "R", "R", "."]
])
test3 = score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]])
test4 = score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]])
test5 = score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]])
test6 = score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]])

check1 = "R:2"
check2 = "Y: 3"
check3 = "No points awarded"
check4 = "R: 4"
check5 = "Y: 1"
check6 = "No points awarded"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")