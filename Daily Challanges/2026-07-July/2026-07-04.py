def kaprekar(number):
    count = 0

    while number != 6174:
        digits = f"{number:04d}"
        large = int("".join(sorted(digits, reverse=True)))
        small = int("".join(sorted(digits)))
        number = large - small
        count += 1

    return count


print(kaprekar(1234))
print(kaprekar(2025))
print(kaprekar(7173))
print(kaprekar(3164))
print(kaprekar(8082))
