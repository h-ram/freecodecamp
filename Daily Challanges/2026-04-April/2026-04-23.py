def get_direction(time1, time2):
    hours1, mins1 = map(int, time1.split(':'))
    hours2, mins2 = map(int, time2.split(':'))
    t1 = hours1*60 + mins1
    t2 = hours2*60 + mins2
    if t1 > t2:
        t2 += 24*60
    right_dist = abs(t2 - t1)
    left_dist = abs(1440 - right_dist)
 
    if right_dist < left_dist:
        return "forward"
    elif left_dist < right_dist:
        return "backward"
    else:
        return "equal"

print(get_direction("10:00", "12:00"))
print(get_direction("11:00", "05:00"))
print(get_direction("00:00", "12:00"))
print(get_direction("15:45", "01:10"))
print(get_direction("03:30", "19:50"))
print(get_direction("06:30", "18:30"))