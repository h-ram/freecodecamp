def get_oldest(people):
    oldest_age = 0
    for person in people:
        name = person["name"]
        age = person["age"] 
        oldest_age = max(oldest_age, age)
    
    oldest_people = []
    for person in people:
        name = person["name"]
        age = person["age"] 
        if age == oldest_age:
            oldest_people.append(name)
    
    return oldest_people

print(get_oldest([{ "name": "Brenda", "age": 40 }]) )
print(get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]))
print(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]))
