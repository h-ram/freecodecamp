def get_fastest_speed(times):
    speeds = [
        320/times[0],
        280/times[1],
        350/times[2],
        300/times[3],
        250/times[4]
    ]
    fastest_speed = max(speeds)
    fastest_seg = speeds.index(fastest_speed) + 1

    result = f"The luger's fastest speed was {fastest_speed:.2f} m/s on segment {fastest_seg}."
    return result


test1 = get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128])
test2 = get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284])
test3 = get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912])
test4 = get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840])
test5 = get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508])

check1 = "The luger's fastest speed was 35.07 m/s on segment 5."
check2 = "The luger's fastest speed was 37.75 m/s on segment 2."
check3 = "The luger's fastest speed was 38.49 m/s on segment 3."
check4 = "The luger's fastest speed was 37.69 m/s on segment 1."
check5 = "The luger's fastest speed was 39.24 m/s on segment 4."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")