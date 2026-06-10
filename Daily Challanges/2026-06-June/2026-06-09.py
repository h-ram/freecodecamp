def get_roommates(people):
    groups = {}
    for person in people:
        g = person["group"]
        if g not in groups:
            groups[g] = []
        groups[g].append(person["name"])
    rooms = []
    for names in groups.values():
        i = 0
        while i + 1 < len(names):
            rooms.append(f"{names[i]} and {names[i + 1]}")
            i += 2

        if i < len(names):
            rooms.append(names[i])

    return rooms


print(get_roommates([
    {"name": "Alice", "group": "A"},
    {"name": "Bob", "group": "B"},
    {"name": "Carol", "group": "A"}
]))

print(get_roommates([
    {"name": "John", "group": "C"},
    {"name": "Julia", "group": "C"},
    {"name": "Jim", "group": "C"}
]))

print(get_roommates([
    {"name": "Adam", "group": "D"},
    {"name": "Abraham", "group": "E"},
    {"name": "Austin", "group": "E"},
    {"name": "Augustus", "group": "D"},
    {"name": "Angelica", "group": "D"},
    {"name": "Aaron", "group": "E"}
]))

print(get_roommates([
    {"name": "Frank", "group": "A"},
    {"name": "Emitt", "group": "B"},
    {"name": "Daria", "group": "F"},
    {"name": "Charles", "group": "D"},
    {"name": "Bailey", "group": "A"},
    {"name": "Albert", "group": "F"}
]))

print(get_roommates([
    {"name": "Kevin", "group": "A"},
    {"name": "Yuri", "group": "A"},
    {"name": "Hugo", "group": "B"},
    {"name": "Violet", "group": "A"},
    {"name": "Brett", "group": "A"},
    {"name": "Wayne", "group": "B"}
]))