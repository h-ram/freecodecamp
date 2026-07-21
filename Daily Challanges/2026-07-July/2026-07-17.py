from datetime import date


def days_until_birthday(today, birthday):
    year, month, day = map(int, today.split("-"))
    birth_month, birth_day = map(int, birthday.split("/"))
    today_date = date(year, month, day)

    def next_birthday(start_year):
        y = start_year
        while True:
            try:
                return date(y, birth_month, birth_day)
            except ValueError:
                y += 1

    birthday_date = next_birthday(year)

    if birthday_date <= today_date:
        birthday_date = next_birthday(birthday_date.year + 1)

    return (birthday_date - today_date).days


print(days_until_birthday("2026-07-16", "9/7"))
print(days_until_birthday("2026-07-16", "3/22"))
print(days_until_birthday("2026-07-16", "7/16"))
print(days_until_birthday("2024-02-28", "3/1"))
print(days_until_birthday("2023-04-24", "12/30"))
print(days_until_birthday("2024-03-01", "2/29"))
print(days_until_birthday("2096-03-01", "2/29"))
