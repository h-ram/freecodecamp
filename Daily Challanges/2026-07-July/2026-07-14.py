def pet_years(pet, age):
    multipliers = {
        "dog": 7,
        "cat": 6,
        "rabbit": 8,
        "hamster": 30,
        "guinea pig": 12,
        "goldfish": 6,
        "bird": 5,
    }
    return age * multipliers[pet]


print(pet_years("dog", 5))
print(pet_years("cat", 9))
print(pet_years("rabbit", 3))
print(pet_years("hamster", 4))
print(pet_years("guinea pig", 5))
print(pet_years("goldfish", 2))
print(pet_years("bird", 1))
