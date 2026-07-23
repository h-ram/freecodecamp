def elevator_stops(current_floor, requested_floors):
    above = sorted([f for f in requested_floors if f > current_floor])
    below = sorted([f for f in requested_floors if f < current_floor], reverse=True)

    if not above:
        up_distance = current_floor - below[-1]
    elif not below:
        up_distance = above[-1] - current_floor
    else:
        up_distance = (above[-1] - current_floor) + (above[-1] - below[-1])

    if not below:
        down_distance = above[-1] - current_floor
    elif not above:
        down_distance = current_floor - below[-1]
    else:
        down_distance = (current_floor - below[-1]) + (above[-1] - below[-1])

    if up_distance <= down_distance:
        return above + below

    return below + above


print(elevator_stops(5, [2, 8, 3, 9]))
print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
print(elevator_stops(1, [4, 8, 3, 6, 9]))
print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))
