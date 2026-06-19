def get_streaming_bill(cart, subscription):
    prices_in_cents = {
        ("HD", "rent"): 399,
        ("HD", "buy"): 1299,
        ("4K", "rent"): 599,
        ("4K", "buy"): 1999,
    }
    discounts = {"none": 0.0, "basic": 0.10, "premium": 0.25}

    total_cents = sum(prices_in_cents[(item["format"], item["type"])] for item in cart)

    total = total_cents / 100
    total *= 1 - discounts[subscription]

    return f"${total:.2f}"


print(get_streaming_bill([{"format": "HD", "type": "rent"}], "none"))
print(
    get_streaming_bill(
        [{"format": "HD", "type": "rent"}, {"format": "HD", "type": "buy"}], "premium"
    )
)
print(
    get_streaming_bill(
        [
            {"format": "HD", "type": "rent"},
            {"format": "HD", "type": "rent"},
            {"format": "HD", "type": "buy"},
        ],
        "basic",
    )
)
print(
    get_streaming_bill(
        [{"format": "4K", "type": "buy"}, {"format": "4K", "type": "buy"}], "premium"
    )
)
print(
    get_streaming_bill(
        [
            {"format": "HD", "type": "rent"},
            {"format": "4K", "type": "rent"},
            {"format": "HD", "type": "buy"},
            {"format": "4K", "type": "buy"},
        ],
        "none",
    )
)
print(
    get_streaming_bill(
        [
            {"format": "HD", "type": "rent"},
            {"format": "4K", "type": "rent"},
            {"format": "HD", "type": "buy"},
            {"format": "4K", "type": "buy"},
            {"format": "HD", "type": "buy"},
        ],
        "basic",
    )
)
