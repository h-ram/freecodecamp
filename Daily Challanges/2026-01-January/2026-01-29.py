def separate_letters_and_numbers(s):
    result = s[0]
    for i in range(1, len(s)):
        if s[i-1].isdigit() != s[i].isdigit():
            result += "-"
        result += s[i]
    return result

test1 = separate_letters_and_numbers("ABC123")
test2 = separate_letters_and_numbers("Route66")
test3 = separate_letters_and_numbers("H3LL0W0RLD")
test4 = separate_letters_and_numbers("a1b2c3d4")

check1 = "ABC-123"
check2 = "Route-66"
check3 = "H-3-LL-0-W-0-RLD"
check4 = "a-1-b-2-c-3-d-4"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")