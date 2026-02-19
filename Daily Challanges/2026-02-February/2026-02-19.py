def avalanche_risk(snow_depth, slope):
    if snow_depth == "Shallow" or slope == "Gentle":
        return "Safe"
    return "Risky"

test1 = avalanche_risk("Shallow", "Gentle")
test2 = avalanche_risk("Shallow", "Steep")
test3 = avalanche_risk("Shallow", "Very Steep")
test4 = avalanche_risk("Moderate", "Gentle")
test5 = avalanche_risk("Moderate", "Steep")
test6 = avalanche_risk("Moderate", "Very Steep")
test7 = avalanche_risk("Deep", "Gentle")
test8 = avalanche_risk("Deep", "Steep")
test9 = avalanche_risk("Deep", "Very Steep")

check1 = "Safe"
check2 = "Safe"
check3 = "Safe"
check4 = "Safe"
check5 = "Risky"
check6 = "Risky"
check7 = "Safe"
check8 = "Risky"
check9 = "Risky"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
print(f"Test9: {test9 == check9}")