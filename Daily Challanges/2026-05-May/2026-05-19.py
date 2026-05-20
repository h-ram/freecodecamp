def sleep_debt(hours_slept, target_hours):
    debt = sum(target_hours - hour for hour in hours_slept)
    debt += target_hours
    return max(0, debt)

print(sleep_debt([6, 6, 6, 6, 6, 6], 8));
print(sleep_debt([6, 7, 8, 4, 8, 6], 7));
print(sleep_debt([10, 10, 9, 10, 9, 11], 9));
print(sleep_debt([8, 7, 6, 7, 6, 8], 6));
print(sleep_debt([8, 9, 10, 9, 10, 7], 7));