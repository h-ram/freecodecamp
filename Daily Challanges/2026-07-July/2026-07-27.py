import math


def is_pronic(n):
    x = math.isqrt(n)
    return x * (x + 1) == n


print(is_pronic(6))
print(is_pronic(15))
print(is_pronic(12))
print(is_pronic(132))
print(is_pronic(80))
print(is_pronic(0))