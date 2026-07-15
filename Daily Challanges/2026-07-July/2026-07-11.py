def five_dice(dice):
    counts = sorted({x: dice.count(x) for x in set(dice)}.values(), reverse=True)
    s = sorted(set(dice))

    if counts == [5]:
        return "five of a kind"
    if counts == [4, 1]:
        return "four of a kind"
    if s == [1, 2, 3, 4, 5] or s == [2, 3, 4, 5, 6]:
        return "large straight"
    if counts == [3, 2]:
        return "full house"
    if any(s[i : i + 4] == list(range(s[i], s[i] + 4)) for i in range(len(s) - 3)):
        return "small straight"
    if counts == [3, 1, 1]:
        return "three of a kind"
    if counts == [2, 2, 1]:
        return "two pair"
    if counts == [2, 1, 1, 1]:
        return "pair"
    return "no pair"


print(five_dice([1, 1, 1, 1, 1]))
print(five_dice([5, 5, 5, 6, 5]))
print(five_dice([2, 5, 6, 4, 3]))
print(five_dice([4, 3, 3, 3, 1]))
print(five_dice([4, 6, 2, 6, 5]))
print(five_dice([1, 4, 5, 6, 2]))
print(five_dice([1, 3, 4, 6, 2]))
print(five_dice([2, 2, 5, 2, 5]))
print(five_dice([6, 4, 5, 6, 4]))
