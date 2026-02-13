def is_balanced(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    first_half = s[:len(s)//2]
    second_half = s[(len(s)+1)//2:]

    first_count = 0
    second_count = 0

    for char in first_half:
        if char.lower() in vowels:
            first_count += 1

    for char in second_half:
        if char.lower() in vowels:
            second_count += 1       
    
    return first_count == second_count


test1 = is_balanced("racecar")
test2 = is_balanced("Lorem Ipsum")
test3 = is_balanced("Kitty Ipsum")
test4 = is_balanced("string")
test5 = is_balanced(" ")
test6 = is_balanced("abcdefghijklmnopqrstuvwxyz")
test7 = is_balanced("123A#b!E&*456-o.U")

check1 = True
check2 = True
check3 = False
check4 = False
check5 = True
check6 = False
check7 = True

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")