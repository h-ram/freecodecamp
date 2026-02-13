
def has_consonant_count(text, target):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    text = text.lower()
    

    for character in text:
        if character not in vowels and character.isalpha():
            count += 1

    return count == target

test1 = has_consonant_count("helloworld", 7)
test2 = has_consonant_count("eieio", 5)
test3 = has_consonant_count("freeCodeCamp Rocks!", 11)
test4 = has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24)
test5 = has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23)


check1 = True
check2 = False
check3 = True
check4 = False
check5 = True


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")