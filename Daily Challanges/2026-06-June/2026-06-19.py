from datetime import datetime, timedelta
from math import ceil


def get_rental_cost(rented, returned, tier):
    pricing = {
        1: {"base": 4.99, "late": 3.99},
        3: {"base": 3.99, "late": 2.99},
        7: {"base": 2.99, "late": 0.99},
    }

    rented_date = datetime.fromisoformat(rented.replace("Z", "+00:00"))
    returned_date = datetime.fromisoformat(returned.replace("Z", "+00:00"))

    due_date = datetime(
        rented_date.year,
        rented_date.month,
        rented_date.day,
        12,
        tzinfo=rented_date.tzinfo,
    ) + timedelta(days=tier)

    late_days = 0

    if returned_date > due_date:
        late_days = ceil((returned_date - due_date).total_seconds() / 86400)

    total = pricing[tier]["base"] + late_days * pricing[tier]["late"]

    return f"${total:.2f}"


print(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1))
print(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1))
print(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3))
print(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3))
print(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7))
print(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7))
