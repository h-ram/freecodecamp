def get_due_date(date_str):
    year, month, day = map(int, date_str.split("-"))

    total_months = (month - 1) + 9
    target_year = year + (total_months // 12)
    target_month = (total_months % 12) + 1

    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    days_in_month = [
        31,
        29 if is_leap(target_year) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]

    max_day = days_in_month[target_month - 1]
    target_day = min(day, max_day)

    return f"{target_year}-{target_month:02d}-{target_day:02d}"


print(get_due_date("2025-03-30"))
print(get_due_date("2025-05-31"))
print(get_due_date("2025-04-27"))
