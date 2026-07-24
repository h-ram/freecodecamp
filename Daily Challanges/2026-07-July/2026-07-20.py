def is_golden_ratio(a, b):
    ratio = max(a, b) / min(a, b)
    return abs(ratio - 1.618) <= 0.01


print(is_golden_ratio(21, 34))
print(is_golden_ratio(15, 20))
print(is_golden_ratio(8, 13))
print(is_golden_ratio(10, 16))
print(is_golden_ratio(1618, 1000))
print(is_golden_ratio(88, 55))
