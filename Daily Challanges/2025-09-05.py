def is_valid_ipv4(ipv4):
    parts = ipv4.split('.')

    if len(parts) != 4:
        return False # not enough dots

    for part in parts:
        if not part.isdigit():
            return False; # not numeric

        if part.lstrip('0') != part and part != '0':
            return False # leading zeroes
            
        if not (0 <= int(part) <= 255):
            return False # out of range
    
    return True

test1 = is_valid_ipv4("192.168.1.1")
test2 = is_valid_ipv4("0.0.0.0")
test3 = is_valid_ipv4("255.01.50.111")
test4 = is_valid_ipv4("255.00.50.111")
test5 = is_valid_ipv4("256.101.50.115")
test6 = is_valid_ipv4("192.168.101.")
test7 = is_valid_ipv4("192168145213")

check1 = True
check2 = True
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")