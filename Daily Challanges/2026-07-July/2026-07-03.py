def migrate_record(default_record, record):
    result = record.copy()

    for key, value in default_record.items():
        if key not in result:
            result[key] = value

    return result


print(migrate_record({"username": "", "posts": 0}, {"verified": True}))
print(migrate_record({"username": "", "posts": 0}, {"username": "camper", "posts": 5}))
print(
    migrate_record(
        {"username": "", "posts": 0, "verified": False}, {"username": "camper"}
    )
)
print(
    migrate_record(
        {"username": "", "posts": 0}, {"username": "camper", "role": "admin"}
    )
)
print(
    migrate_record(
        {
            "username": "",
            "email": "",
            "posts": 0,
            "verified": False,
            "role": "user",
            "banned": False,
        },
        {"username": "camper", "email": "camper@freecodecamp.org", "role": "admin"},
    )
)
