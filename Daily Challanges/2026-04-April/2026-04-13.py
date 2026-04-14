def get_initials(name):
    parts = name.split(' ')
    initials = []
    for part in parts:
        initials.append(part[0].upper() + '.')
    return "".join(initials)

print(get_initials("Tommy Millwood"))
print(get_initials("Savanna Puddlesplash"))
print(get_initials("Dragon"))