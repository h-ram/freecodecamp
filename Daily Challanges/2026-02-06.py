def get_flag(code):
    code = code.upper()
    return ''.join(chr(ord(c) + 127397) for c in code)

test1 = get_flag("AL")
test2 = get_flag("AD")
test3 = get_flag("AR")
test4 = get_flag("AM")
test5 = get_flag("AU")

check1 = "🇦🇱"
check2 = "🇦🇩"
check3 = "🇦🇷"
check4 = "🇦🇲"
check5 = "🇦🇺"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")