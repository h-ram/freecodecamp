def exact_change(amount):
    coins = [1, 5, 10, 25]
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


print(exact_change(3))
print(exact_change(9))
print(exact_change(17))
print(exact_change(39))
print(exact_change(61))
print(exact_change(99))
