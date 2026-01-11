
def speed_check(speed_mph, speed_limit_kph):
    speed_kph = int(speed_mph * 1.60934)

    message = ""
    if speed_kph <= speed_limit_kph:
        message =  "Not Speeding"
    elif speed_kph <= speed_limit_kph+5:
        message = "Warning"
    else:
        message = "Ticket"

    print("speed:", speed_kph)
    print("limit:", speed_limit_kph)
    print("verdict:", message, "\n")

    return message



test1 = speed_check(30, 70)
test2 = speed_check(40, 60)
test3 = speed_check(40, 65)
test4 = speed_check(60, 90)
test5 = speed_check(65, 100)
test6 = speed_check(88, 40)


check1 = "Not Speeding"
check2 = "Warning"
check3 = "Not Speeding"
check4 = "Ticket"
check5 = "Warning"
check6 = "Ticket"


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")