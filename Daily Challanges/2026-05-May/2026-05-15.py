MENU = [
    ("cold brew", 4.50),
    ("oat latte", 5.00),
    ("cappuccino", 4.75),
    ("espresso", 3.00),
    ("vanilla syrup", 0.75),
    ("caramel drizzle", 0.60),
    ("extra shot", 0.50),
    ("oat milk", 0.75),
    ("cream", 0.75),
]


def format_coffee_order(order):
    text = order.lower()
    items = []
    total = 0
    for name, price in MENU:
        if name in text:
            items.append(name)
            total += price

    return f"{' + '.join(items)}: ${total:.2f}"


print(
    format_coffee_order(
        "I'd like an oat latte with vanilla syrup and an extra shot please."
    )
)
