import math
def calculate_parking_fee(park_time, pickup_time):
    cost = 0
    park_minutes = int(park_time[:2])*60 + int(park_time[3:])
    pick_minutes = int(pickup_time[:2])*60 + int(pickup_time[3:])
    if pickup_time < park_time:
        cost += 10
        pick_minutes += 24*60
    diff = pick_minutes - park_minutes
    cost += math.ceil(diff / 60) * 3
    cost = max(cost , 5);
    return f"${cost}"

test1 = calculate_parking_fee("09:00", "11:00")
test2 = calculate_parking_fee("10:00", "10:30")
test3 = calculate_parking_fee("08:10", "10:45")
test4 = calculate_parking_fee("14:40", "23:10")
test5 = calculate_parking_fee("18:15", "01:30")
test6 = calculate_parking_fee("11:11", "11:10")

check1 = "$6"
check2 = "$5"
check3 = "$9"
check4 = "$27"
check5 = "$34"
check6 = "$82"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")