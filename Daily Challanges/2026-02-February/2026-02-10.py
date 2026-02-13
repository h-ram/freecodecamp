
def totalSecs(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_relative_results(results):
    winner_secs = totalSecs(results[0])
    times = ["0"]
    for i in range(1, len(results)):
        player_secs = totalSecs(results[i])
        diff =  player_secs - winner_secs
        minutes = diff // 60
        secs = diff % 60
        times.append(f"+{minutes}:{secs:02d}")

    return times

test1 = get_relative_results(["1:25:32", "1:26:10", "1:27:05"])
test2 = get_relative_results(["1:00:01", "1:00:05", "1:00:10"])
test3 = get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"])
test4 = get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"])
test5 = get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"])

print(test1)
check1 = ["0", "+0:38", "+1:33"]
check2 = ["0", "+0:04", "+0:09"]
check3 = ["0", "+0:17", "+0:42", "+2:05"]
check4 = ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"]
check5 = ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")