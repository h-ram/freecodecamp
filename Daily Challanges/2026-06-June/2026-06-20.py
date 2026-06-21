def prime_factorization(n):
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


print(prime_factorization(20))
print(prime_factorization(17))
print(prime_factorization(15))
print(prime_factorization(35))
print(prime_factorization(999))
print(prime_factorization(360))
print(prime_factorization(510510))
