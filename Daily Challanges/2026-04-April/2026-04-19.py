def get_unique_climbs(steps):
    table = [1,2]
    for step in range(2, steps):
        table.append(table[-1] + table[-2])
    return table[-1]

print(get_unique_climbs(4))
print(get_unique_climbs(5))
print(get_unique_climbs(10))