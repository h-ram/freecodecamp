from datetime import datetime, timedelta
from collections import defaultdict

def digital_detox(logs):
    times = sorted(datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in logs)

    for i in range(1, len(times)):
        if times[i] - times[i - 1] < timedelta(hours=4):
            return False

    per_day = defaultdict(int)
    for t in times:
        per_day[t.date()] += 1
        if per_day[t.date()] > 2:
            return False

    return True


test1 = digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])
test2 = digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"])
test3 = digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])
test4 = digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])
test5 = digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
test6 = digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])

check1 = True
check2 = False
check3 = True
check4 = False
check5 = True
check6 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")