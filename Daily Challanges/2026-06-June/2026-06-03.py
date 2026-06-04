def is_valid_schema(obj):
    return (
        isinstance(obj, dict)
        and isinstance(obj.get("username"), str)
        and isinstance(obj.get("posts"), (int, float))
        and isinstance(obj.get("verified"), bool)
        and obj.get("role") in {
            "user",
            "creator",
            "moderator",
            "staff",
            "admin"
        }
    )

print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"})) 
print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70})) 