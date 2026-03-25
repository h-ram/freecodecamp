from datetime import datetime, timedelta
def can_retake(finish_time, current_time):
    fdate = datetime.fromisoformat(finish_time)
    cdate = datetime.fromisoformat(current_time)
    diff = cdate-fdate
    return diff >= timedelta(hours=48)

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))