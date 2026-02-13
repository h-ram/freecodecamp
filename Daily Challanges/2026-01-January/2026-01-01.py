def resolution_streak(days):
    streak = 0
    for day, (steps, screen_time, pages) in enumerate(days):
        is_success = steps >= 10000 and screen_time <= 120 and pages >= 5
        if not is_success:
            return f"Resolution failed on day {day+1}: {streak} day streak."
        streak += 1
    return f"Resolution on track: {streak} day streak."


test1 = resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]])
test2 = resolution_streak([[10000, 120, 5], [10950, 121, 11]])
test3 = resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]])
test4 = resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]])
test5 = resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]])


check1 = "Resolution on track: 3 day streak."
check2 = "Resolution failed on day 2: 1 day streak."
check3 = "Resolution failed on day 3: 2 day streak."
check4 = "Resolution failed on day 4: 3 day streak."
check5 = "Resolution on track: 10 day streak."


print(test1)
print(test2)
print(test3)
print(test4)
print(test5)


print()
print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")

