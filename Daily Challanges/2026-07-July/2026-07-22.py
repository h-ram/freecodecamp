def piggy_bank(coins):
    total = (
        coins.get("pennies", 0)
        + coins.get("nickels", 0) * 5
        + coins.get("dimes", 0) * 10
        + coins.get("quarters", 0) * 25
    )

    return f"${total / 100:.2f}"


print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))
print(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}))
print(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}))
print(piggy_bank({}))
print(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}))
