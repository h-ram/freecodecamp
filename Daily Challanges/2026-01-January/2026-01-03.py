

def find_left_handed_seats(table):

    count = 0
    coords = []
    # top row
    for i in range(3):
        if table[0][i] == 'U' and table[0][i+1] in ['L','U']:
            count += 1 
            coords.append((0,i))

    if table[0][3] == 'U':
        count += 1
        coords.append((0,3))

    # bottom row
    for i in range(1,4):
        if table[1][i] == 'U' and table[1][i-1] in ['L', 'U']:
            count += 1
            coords.append((1,i))
    if table[1][0] == 'U':
        count += 1
        coords.append((1,0))

    print(table[0])
    print(table[1])
    print(*coords)

    print("Available seats:", count)
    print()
    return count



test1 = find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]])
test2 = find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]])
test3 = find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]])
test4 = find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]])
test5 = find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]])

check1 = 2
check2 = 8
check3 = 0
check4 = 1
check5 = 5

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")