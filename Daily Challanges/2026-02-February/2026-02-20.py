def is_valid_trick(trick_name):
    valid_firsts = [
        "Misty",
        "Ghost",
        "Thunder",
        "Solar",
        "Sky",
        "Phantom",
        "Frozen",
        "Polar"
    ];

    valid_seconds = [
        "Twister",
        "Icequake",
        "Avalanche",
        "Vortex",
        "Snowstorm",
        "Frostbite",
        "Blizzard",
        "Shadow"
    ];

    word1, word2 = trick_name.split(' ')
    return word1 in valid_firsts and word2 in valid_seconds

test1 = is_valid_trick("Polar Vortex")
test2 = is_valid_trick("Solar Icequake")
test3 = is_valid_trick("Thunder Blizzard")
test4 = is_valid_trick("Phantom Frostbite")
test5 = is_valid_trick("Ghost Avalanche")
test6 = is_valid_trick("Snowstorm Shadow")
test7 = is_valid_trick("Solar Sky")

check1 = True
check2 = True
check3 = True
check4 = True
check5 = True
check6 = False
check7 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")