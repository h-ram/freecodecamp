def is_valid_schema(obj):
    roles = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False

    users = obj.get("users")

    if not isinstance(users, list):
        return False

    for user in users:
        if not isinstance(user, dict):
            return False

        required = ["username", "posts", "verified", "role", "badges"]
        if not all(key in user for key in required):
            return False

        if not isinstance(user["username"], str):
            return False

        if not isinstance(user["posts"], (int, float)) or isinstance(
            user["posts"], bool
        ):
            return False

        if not isinstance(user["verified"], bool):
            return False

        if user["role"] not in roles:
            return False

        if "supporter" in user and not isinstance(user["supporter"], bool):
            return False

        if not isinstance(user["badges"], list):
            return False

        if not all(isinstance(badge, str) for badge in user["badges"]):
            return False

    return True


print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "ron",
                    "posts": 14,
                    "verified": True,
                    "role": "creator",
                    "badges": ["early-adopter"],
                },
                {
                    "username": "cher",
                    "posts": 25,
                    "verified": True,
                    "role": "moderator",
                    "supporter": True,
                    "followers": 20,
                    "badges": ["helper"],
                },
            ]
        }
    )
)

print(is_valid_schema({"users": []}))

print(
    is_valid_schema(
        {
            "users": {
                "username": "anne",
                "posts": 0,
                "verified": False,
                "role": "user",
                "supporter": False,
                "badges": [],
            }
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "tony",
                    "posts": 10,
                    "verified": True,
                    "role": "creator",
                    "supporter": True,
                    "badges": ["liked", 6],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "ursula",
                    "posts": 3,
                    "verified": False,
                    "role": "user",
                    "supporter": "false",
                    "badges": ["comeback"],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "benny",
                    "posts": 55,
                    "verified": True,
                    "role": "superstar",
                    "supporter": True,
                    "badges": ["veteran"],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "chase",
                    "posts": 1,
                    "verified": "yes",
                    "role": "staff",
                    "supporter": False,
                    "badges": ["superstar"],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "carla",
                    "posts": "10",
                    "verified": False,
                    "role": "user",
                    "supporter": False,
                    "badges": ["newbie"],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "posts": 4,
                    "verified": False,
                    "role": "admin",
                    "supporter": False,
                    "badges": ["superuser", "veteran"],
                }
            ]
        }
    )
)

print(
    is_valid_schema(
        {
            "users": [
                {
                    "username": "harold",
                    "posts": 80,
                    "verified": True,
                    "role": "creator",
                    "supporter": True,
                    "badges": ["liked", "hero"],
                },
                {
                    "username": "kim",
                    "posts": 11,
                    "verified": False,
                    "role": "admin",
                    "supporter": True,
                    "badges": ["first"],
                },
                {},
            ]
        }
    )
)
