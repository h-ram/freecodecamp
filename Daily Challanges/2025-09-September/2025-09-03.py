def is_pangram(sentence, letters):
    used = {char.lower() for char in sentence if char.isalpha()}
    allowed = set(letters.lower())
    return used == allowed

test1 = is_pangram("hello", "helo")
test2 = is_pangram("hello", "hel")
test3 = is_pangram("hello", "helow")
test4 = is_pangram("hello world", "helowrd")
test5 = is_pangram("Hello World!", "helowrd")
test6 = is_pangram("Hello World!", "heliowrd")
test7 = is_pangram("freeCodeCamp", "frcdmp")
test8 = is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz")

check1 = True
check2 = False
check3 = False
check4 = True
check5 = True
check6 = False
check7 = False
check8 = True

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")