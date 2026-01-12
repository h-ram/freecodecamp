def get_number_of_plants(field_size, unit, crop):
    size = 1
    if unit == "acres":
        size = field_size * 4046.86
    else:
        size = field_size * 10000
    
    crops = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    total_possible_plants = int(size / crops[crop])
    return total_possible_plants


test1 = get_number_of_plants(1, "acres", "corn")
test2 = get_number_of_plants(2, "hectares", "lettuce")
test3 = get_number_of_plants(20, "acres", "soybeans")
test4 = get_number_of_plants(3.75, "hectares", "tomatoes")
test5 = get_number_of_plants(16.75, "acres", "tomatoes")

check1 = 4046
check2 = 100000
check3 = 161874
check4 = 150000
check5 = 271139


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")