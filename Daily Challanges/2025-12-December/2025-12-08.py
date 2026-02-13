def convert_to_kgs(lbs):
    kgs = round(lbs * 0.453592,2)

    pound = "pound" if lbs == 1 else "pounds"
    kilos = "kilogram" if kgs == 1 else "kilograms"
    response = f"{lbs} {pound} equals {kgs:.2f} {kilos}."
    return response

test1 = convert_to_kgs(1)
test2 = convert_to_kgs(0)
test3 = convert_to_kgs(100)
test4 = convert_to_kgs(2.5)
test5 = convert_to_kgs(2.20462)

check1 = "1 pound equals 0.45 kilograms."
check2 = "0 pounds equals 0.00 kilograms."
check3 = "100 pounds equals 45.36 kilograms."
check4 = "2.5 pounds equals 1.13 kilograms."
check5 = "2.20462 pounds equals 1.00 kilogram."

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")