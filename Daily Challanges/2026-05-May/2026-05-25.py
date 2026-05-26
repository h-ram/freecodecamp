def guess_number(secret, guess):
    return "higher" if secret > guess else "lower" if secret < guess else "you got it!"

print(guess_number(50, 30))
print(guess_number(85, 99))
print(guess_number(2026, 2026))
print(guess_number(92904, 11283))