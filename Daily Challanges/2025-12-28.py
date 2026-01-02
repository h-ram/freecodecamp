def to_screaming_snake_case(variable_name):

    new_str = new_str = [variable_name[0].upper()]
    for i in range(1, len(variable_name)):
        char = variable_name[i]
        if char == "-" or char == "_":
            new_str.append("_")
            continue
        elif char.isupper():
            new_str.append("_")
        new_str.append(char.upper())
    return "".join(new_str)


test1 = to_screaming_snake_case("userEmail")
test2 = to_screaming_snake_case("UserPassword")
test3 = to_screaming_snake_case("user_id")
test4 = to_screaming_snake_case("user-address")
test5 = to_screaming_snake_case("username")

check1 = "USER_EMAIL"
check2 = "USER_PASSWORD"
check3 = "USER_ID"
check4 = "USER_ADDRESS"
check5 = "USERNAME"


print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print()

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
