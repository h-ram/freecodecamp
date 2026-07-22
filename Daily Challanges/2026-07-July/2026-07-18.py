def get_odds(dice, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for _ in range(dice):
        next_dp = [0] * (target + 1)
        for total in range(target + 1):
            if dp[total]:
                for face in range(1, 7):
                    if total + face <= target:
                        next_dp[total + face] += dp[total]
        dp = next_dp

    total_outcomes = 6**dice
    ways = dp[target]
    odds = round(total_outcomes / ways)

    return f"1 in {odds}"


print(get_odds(1, 5))
print(get_odds(2, 4))
print(get_odds(3, 10))
print(get_odds(4, 7))
print(get_odds(5, 26))
print(get_odds(6, 35))
