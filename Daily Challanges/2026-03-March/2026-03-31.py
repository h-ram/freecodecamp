def wake_up_alarm(alarm: str, wake: str) -> str:
    ah, am = map(int, alarm.split(":"))
    wh, wm = map(int, wake.split(":"))

    alarm_minutes = ah * 60 + am
    wake_minutes = wh * 60 + wm
    diff = wake_minutes - alarm_minutes

    if diff < 0:
        return "early"
    elif diff <= 10:
        return "on time"
    else:
        return "late"
