def is_narcissistic(n):
    digits = list(map(int, str(n)))
    n_digits = len(digits)
    raised_sum = 0
    for digit in digits:
        raised_sum += digit ** n_digits
    return raised_sum == n

print(is_narcissistic(153))
print(is_narcissistic(154))