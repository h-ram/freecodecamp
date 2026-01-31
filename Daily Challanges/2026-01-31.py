def get_sign(date_str):
    month, day = map(int, date_str.split('-')[1:])
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:  
        return "Pisces"

test1 = get_sign("2026-01-31")
test2 = get_sign("2001-06-10")
test3 = get_sign("1985-09-07")
test4 = get_sign("2023-03-19")
test5 = get_sign("2045-11-05")
test6 = get_sign("1985-12-06")
test7 = get_sign("2025-12-30")
test8 = get_sign("2018-10-08")
test9 = get_sign("1958-05-04")

check1 = "Aquarius"
check2 = "Gemini"
check3 = "Virgo"
check4 = "Pisces"
check5 = "Scorpio"
check6 = "Sagittarius"
check7 = "Capricorn"
check8 = "Libra"
check9 = "Taurus"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
print(f"Test9: {test9 == check9}")