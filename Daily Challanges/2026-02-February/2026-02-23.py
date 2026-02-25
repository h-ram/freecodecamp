def can_donate(donor, recipient):
    valid_donors = {
        "O": ["A","B","AB", "O"],
        "A": ["A","AB"],
        "B": ["B","AB"],
        "AB": ["AB"],
    }
    if recipient[:-1] in valid_donors[donor[:-1]] and not (donor[-1] + recipient[-1] == "+-"):
        return True
    else:
        return False

test1 = can_donate("B+", "B+")
test2 = can_donate("O-", "AB-")
test3 = can_donate("O+", "A-")
test4 = can_donate("A+", "AB+")
test5 = can_donate("A-", "B-")
test6 = can_donate("B-", "AB+")
test7 = can_donate("B-", "A+")
test8 = can_donate("O-", "O+")
test9 = can_donate("O+", "O-")
test10 = can_donate("AB+", "AB-")

check1 = True
check2 = True
check3 = False
check4 = True
check5 = False
check6 = True
check7 = False
check8 = True
check9 = False
check10 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
print(f"Test9: {test9 == check9}")
print(f"Test10: {test10 == check10}")