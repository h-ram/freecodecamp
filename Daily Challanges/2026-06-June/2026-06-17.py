def cast(spells):
    score = {
        "f": (3, "D"),
        "l": (3, "D"),
        "i": (2, "C"),
        "w": (2, "C"),
        "h": (1, "R"),
        "s": (1, "R"),
    }

    total = 0
    multiplier = 1
    prev_category = None

    for spell in spells:
        base, category = score[spell]

        if prev_category is not None:
            if category != prev_category:
                multiplier += 1
            else:
                multiplier = 1

        total += base * multiplier
        prev_category = category

    return total


print(cast("fihwl"))
print(cast("lwswfi"))
print(cast("wislhfl"))
print(cast("sihwlih"))
print(cast("wishlfihwslwifihl"))