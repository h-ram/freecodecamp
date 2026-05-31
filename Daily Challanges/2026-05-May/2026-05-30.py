from collections import Counter


def get_best_hand(cards):
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    rank_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    values = sorted(rank_values[r] for r in ranks)
    is_flush = len(set(suits)) == 1

    is_straight = False
    if len(set(values)) == 5:
        if values[-1] - values[0] == 4:
            is_straight = True
        elif values == [2, 3, 4, 5, 14]:
            is_straight = True

    counts = sorted(Counter(ranks).values(), reverse=True)

    if is_flush and set(ranks) == {"A", "K", "Q", "J", "T"}:
        return "Royal Flush"

    if is_flush and is_straight:
        return "Straight Flush"

    if counts == [4, 1]:
        return "Four of a Kind"

    if counts == [3, 2]:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if counts == [3, 1, 1]:
        return "Three of a Kind"

    if counts == [2, 2, 1]:
        return "Two Pair"

    if counts == [2, 1, 1, 1]:
        return "Pair"

    return "High Card"


print(get_best_hand(["7s", "7h", "7d", "2c", "5h"]))
print(get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]))
print(get_best_hand(["2h", "5h", "7h", "9h", "Jh"]))
