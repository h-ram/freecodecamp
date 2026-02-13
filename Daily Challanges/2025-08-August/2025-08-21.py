def mile_pace(miles, duration):
    minutes, seconds = duration.split(':')

    total_seconds = int(minutes)*60 + int(seconds)

    total_pace_seconds = total_seconds // miles

    pace_minutes = int(total_pace_seconds // 60)
    pace_seconds = int(total_pace_seconds - pace_minutes * 60)

    return f"{pace_minutes:02d}:{pace_seconds:02d}"


test1 = mile_pace(3, "24:00")
test2 = mile_pace(1, "06:45")
test3 = mile_pace(2, "07:00")
test4 = mile_pace(26.2, "120:35")

check1 = "08:00"
check2 = "06:45"
check3 = "03:30"
check4 = "04:36"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")