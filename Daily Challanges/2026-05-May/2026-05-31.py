from math import comb
def get_combinations(n):
    return comb(2 * n, n) // (n + 1)

print(get_combinations(0))  # 1
print(get_combinations(1))  # 1
print(get_combinations(2))  # 2
print(get_combinations(3))  # 5
print(get_combinations(4))  # 14