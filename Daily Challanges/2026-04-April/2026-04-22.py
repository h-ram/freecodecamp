SCORE = {
    "bottle": 10,
    "can": 6,
    "bag": 8,
    "tire": 35,
    "straw": 4,
    "cardboard": 3,
    "newspaper": 3,
    "shoe": 12,
    "electronics": 25,
    "battery": 18,
    "mattress": 38,
}


def get_cleanup_score(items):
    final_score = 0
    streak = 0
    prev = None
    for i in range(len(items)):
        value = 0
        is_rare = isinstance(items[i], list)

        if is_rare:
            value = items[i][1]
            streak = 0
            prev = None
        else:
            if items[i] == prev:
                streak += 1
            else:
                streak = 1
            value = SCORE[items[i]] + (streak - 1)
            prev = items[i]
        multiplier = 1
        if (i + 1) % 5 == 0:
            multiplier = (i + 1) // 5 + 1
        final_score += value * multiplier
    return final_score


print(get_cleanup_score(["bottle", "straw", "shoe", "battery"]))
print(get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]))
print(
    get_cleanup_score(
        ["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]
    )
)
print(
    get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]])
)
