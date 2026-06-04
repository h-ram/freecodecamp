def is_valid_schema(obj):
    roles = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj.get("username"), str):
        return False

    if not isinstance(obj.get("posts"), (int, float)) or isinstance(
        obj.get("posts"), bool
    ):
        return False

    if not isinstance(obj.get("verified"), bool):
        return False

    if obj.get("role") not in roles:
        return False

    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    return True


print(
    is_valid_schema(
        {
            "username": "vivian",
            "posts": 1,
            "verified": False,
            "role": "user",
            "supporter": True,
        }
    )
)

print(
    is_valid_schema(
        {"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}
    )
)

print(
    is_valid_schema(
        {
            "username": "julia",
            "posts": 50,
            "verified": True,
            "role": "admin",
            "supporter": "true",
        }
    )
)
