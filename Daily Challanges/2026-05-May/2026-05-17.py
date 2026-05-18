from datetime import datetime, timezone

def mongo_id_to_date(s):
    timestamp = int(s[:8], 16)
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

print(mongo_id_to_date("6a094b50bcf86cd799439011"))