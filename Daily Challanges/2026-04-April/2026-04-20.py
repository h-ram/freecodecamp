DICTIONARY = {
    "NASA": "National Avocado Storage Authority",
    "CIA": "Cats Infiltration Agency",
    "FBI": "Fluffy Beanbag Inspectors",
    "DOJ": "Department Of Jelly",
    "WHO": "Wild Honey Organization",
    "EPA": "Eating Pancakes Administration",
}


def find_org(acronym):
    return DICTIONARY[acronym]


print(find_org("NASA"))
print(find_org("CIA"))
print(find_org("FBI"))
