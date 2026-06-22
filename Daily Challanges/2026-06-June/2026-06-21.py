def get_daytime_hours(latitude):
    daylight = round((12 + (latitude / 90) * 12) / 2) * 2
    sunrise = 12 - daylight / 2
    sunset = 12 + daylight / 2

    result = ""

    for h in range(24):
        result += "☀️" if sunrise <= h < sunset else "🌑"

    return result


print(get_daytime_hours(0))
print(get_daytime_hours(90))
print(get_daytime_hours(-90))
print(get_daytime_hours(-33))
print(get_daytime_hours(66.5))
print(get_daytime_hours(40))
print(get_daytime_hours(-50))
