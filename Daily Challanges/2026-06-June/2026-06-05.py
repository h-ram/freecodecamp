def is_valid_schema(obj):
    roles = {"user", "creator", "moderator", "staff", "admin"}
    required = ["username", "posts", "verified", "role", "badges"]
    if not all(key in obj for key in required):
        return False
    if not isinstance(obj["username"], str):
        return False
    if not isinstance(obj["posts"], (int, float)) or isinstance(obj["posts"], bool):
        return False
    if not isinstance(obj["verified"], bool):
        return False
    if obj["role"] not in roles:
        return False
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False
    if not isinstance(obj["badges"], list):
        return False
    if not all(isinstance(badge, str) for badge in obj["badges"]):
        return False
    return True


print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}))
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}))
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}))
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}))
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}))
print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}))
print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]}))
print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]}))
print(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]}))
print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]}))