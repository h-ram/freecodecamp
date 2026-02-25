from datetime import datetime, timedelta

def count_business_days(start, end):
    start = datetime.strptime(start, "%Y-%m-%d").date()
    end = datetime.strptime(end, "%Y-%m-%d").date()
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # 0=monday
            count += 1
        current += timedelta(days=1)
    return count

test1 = count_business_days("2026-02-24", "2026-02-26")
test2 = count_business_days("2026-02-24", "2026-02-28")
test3 = count_business_days("2026-02-21", "2026-03-01")
test4 = count_business_days("2026-03-08", "2026-03-17")
test5 = count_business_days("2026-02-24", "2027-02-24")

check1 = 3
check2 = 4
check3 = 5
check4 = 7
check5 = 262

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")