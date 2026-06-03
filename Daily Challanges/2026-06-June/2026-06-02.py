def is_valid_schema(obj):
    return (
        isinstance(obj, dict)
        and "username" in obj
        and "posts" in obj
        and "verified" in obj
        and isinstance(obj["username"], str)
        and isinstance(obj["posts"], (int, float))
        and not isinstance(obj["posts"], bool)
        and isinstance(obj["verified"], bool)
    )


print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))
print(
    is_valid_schema(
        {"username": "carol", "posts": 15, "verified": True, "followers": 25}
    )
)
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))
print(is_valid_schema({"username": "bill", "verified": True}))
print(is_valid_schema({"username": "fred", "verified": True}))
print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))
