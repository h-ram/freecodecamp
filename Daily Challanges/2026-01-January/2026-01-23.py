def is_valid_hex(s):
    hex_chars = '0123456789ABCDEF'

    if s[0] != '#':
        return False
    
    hex_part = s[1:]
    if not 3 <= len(hex_part) <= 6:
        return False

    for char in hex_part:
        if char.upper() not in hex_chars:
            return False
    return True



test1 = is_valid_hex("#123")
test2 = is_valid_hex("#123abc")
test3 = is_valid_hex("#ABCDEF")
test4 = is_valid_hex("#0a1B2c")
test5 = is_valid_hex("#12G")
test6 = is_valid_hex("#1234567")
test7 = is_valid_hex("#12 3")
test8 = is_valid_hex("fff")

check1 = True
check2 = True
check3 = True
check4 = True
check5 = False
check6 = False
check7 = False
check8 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
