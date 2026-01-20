def to_consonant_case(s):
    vowels = "aeiouAEIOU"

    result = ""
    for char in s:
        if char == '-':
            result += '_'
        elif char in vowels:
            result += char.lower()
        else: 
            result += char.upper()
    return result

test1 = to_consonant_case("helloworld")
test2 = to_consonant_case("HELLOWORLD")
test3 = to_consonant_case("_hElLO-WOrlD-")
test4 = to_consonant_case("_~-generic_~-variable_~-name_~-here-~_")

check1 = "HeLLoWoRLD"
check2 = "HeLLoWoRLD"
check3 = "_HeLLo_WoRLD_"
check4 = "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")