def check_eligibility(athlete_weights, sled_weight):
    n_athletes = len(athlete_weights)
    sum_weights = sum(athlete_weights)
    match n_athletes:
        case 1:
            if sled_weight < 162:
                return "Not Eligible"
            if sum_weights + sled_weight > 247:
                return "Not Eligible"
        case 2:
            if sled_weight < 170:
                return "Not Eligible"
            if sum_weights + sled_weight > 390 :
                return "Not Eligible"
        case 4:
            if sled_weight < 210:
                return "Not Eligible"
            if sum_weights + sled_weight > 630:
                return "Not Eligible"
        case _:
            return "Not Eligible"
    return "Eligible"

test1 = check_eligibility([78], 165)
test2 = check_eligibility([80], 160)
test3 = check_eligibility([80], 170)
test4 = check_eligibility([85, 90], 170)
test5 = check_eligibility([85, 95], 168)
test6 = check_eligibility([112, 97], 185)
test7 = check_eligibility([110, 102, 90, 106], 222)
test8 = check_eligibility([106, 99, 90, 88], 205)
test9 = check_eligibility([106, 99, 103, 96], 227)

check1 = "Eligible"
check2 = "Not Eligible"
check3 = "Not Eligible"
check4 = "Eligible"
check5 = "Not Eligible"
check6 = "Not Eligible"
check7 = "Eligible"
check8 = "Not Eligible"
check9 = "Not Eligible"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
print(f"Test9: {test9 == check9}")