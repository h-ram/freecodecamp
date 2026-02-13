def get_average_grade(scores):
    avg = sum(scores) / len(scores)

    if avg >= 97: return "A+"
    if avg >= 93: return "A"
    if avg >= 90: return "A-"
    if avg >= 87: return "B+"
    if avg >= 83: return "B"
    if avg >= 80: return "B-"
    if avg >= 77: return "C+"
    if avg >= 73: return "C"
    if avg >= 70: return "C-"
    if avg >= 67: return "D+"
    if avg >= 63: return "D"
    if avg >= 60: return "D-"
    return "F"

test1 = get_average_grade([92, 91, 90, 94, 89, 93])
test2 = get_average_grade([84, 89, 85, 100, 91, 88, 79])
test3 = get_average_grade([63, 69, 65, 66, 71, 64, 65])
test4 = get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100])
test5 = get_average_grade([75, 100, 88, 79, 80, 78, 64, 60])
test6 = get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59])

check1 = "A-"
check2 = "B+"
check3 = "D"
check4 = "A+"
check5 = "C+"
check6 = "F"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
