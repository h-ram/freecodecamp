def round_to_nearest_multiple(n, m):
    lower = (n // m) * m
    upper = lower + m
    if n - lower < upper - n:
        return lower
    return upper


print(round_to_nearest_multiple(5, 3))
print(round_to_nearest_multiple(17, 4))
print(round_to_nearest_multiple(43, 5))
print(round_to_nearest_multiple(38, 11))
print(round_to_nearest_multiple(93, 12))
