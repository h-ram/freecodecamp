def get_shadow(time):
    hour = int(time.split(":")[0])
    is_half = time.split(":")[1] == "30"
    length = abs(hour - 12 + 1 / 2 * is_half) ** 3
    length = length if is_half else int(length)
    direction = "east" if hour > 12 else "west"

    if hour < 6 or hour >= 18 or hour == 12:
        return "No shadow"
    else:
        return f"{length}ft {direction}"


print(get_shadow("10:00"))
print(get_shadow("15:00"))
print(get_shadow("17:30"))
print(get_shadow("06:00"))
print(get_shadow("12:00"))
print(get_shadow("18:00"))
print(get_shadow("00:00"))
