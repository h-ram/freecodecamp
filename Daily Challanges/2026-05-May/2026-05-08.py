def medication_reminder(medications, current_time):
    def to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    now = to_min(current_time)
    best_name = ""
    best_wait = float("inf")

    for name, last in medications:
        last = to_min(last)

        if name == "Mergeflictamine":
            next_t = last + 240
            while next_t <= now:
                next_t += 240
        elif name == "Deployxitrin":
            schedule = [480, 960]
            next_t = next((t for t in schedule if t > now), schedule[0] + 1440)
        else:
            schedule = [420, 780, 1260]
            next_t = next((t for t in schedule if t > now), schedule[0] + 1440)

        wait = next_t - now

        if wait < best_wait:
            best_wait = wait
            best_name = name

    return f"{best_name} in {best_wait//60}h {best_wait%60}m"