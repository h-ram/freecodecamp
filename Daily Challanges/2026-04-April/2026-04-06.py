def get_day_of_week(timestamp):
    days = [
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
    ]
    days_since_epoch = timestamp // (1000 * 60 * 60 * 24)
    return days[days_since_epoch % 7]
