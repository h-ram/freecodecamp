def is_valid_schema(obj):
    return isinstance(obj, dict) and isinstance(obj.get("username"), str)

print(is_valid_schema({"username": "bob"}))
print(is_valid_schema({"posts": 25}))