def string_sum(s):
    total = 0

    cache = ""
    for i, char in enumerate(s):
        if char.isdigit():
            cache += char
        else:
            total += 0 if cache == '' else int(cache)
            cache = ""
    total += 0 if cache == '' else int(cache)

    return total

print(string_sum("3apples2bananas"), 5)
print(string_sum("10cats5dogs2birds"), 17)
print(string_sum("125344"), 125344)