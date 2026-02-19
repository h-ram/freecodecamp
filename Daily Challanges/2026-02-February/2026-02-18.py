import math

def calculate_start_delays(jump_scores):
    best_score = max(jump_scores)
    delays = [math.ceil((best_score - score)*1.5) for score in jump_scores]
    return delays

test1 = calculate_start_delays([120, 110, 125])
test2 = calculate_start_delays([118, 125, 122, 120])
test3 = calculate_start_delays([100, 105, 95, 110, 120, 115, 108])
test4 = calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124])

check1 = [8, 23, 0]
check2 = [11, 0, 5, 8]
check3 = [30, 23, 38, 15, 0, 8, 18]
check4 = [3, 11, 6, 18, 21, 15, 8, 26, 0, 12]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")