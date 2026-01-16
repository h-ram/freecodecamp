def are_anagrams(str1, str2):

    return sorted(str1.lower()) == sorted(str2.lower())


test1 = are_anagrams("listen", "silent")
test2 = are_anagrams("School master", "The classroom")
test3 = are_anagrams("A gentleman", "Elegant man")
test4 = are_anagrams("Hello", "World")
test5 = are_anagrams("Hello", "World")
test6 = are_anagrams("apple", "banana")

check1 = True
check2 = True
check3 = True
check4 = False
check5 = False
check6 = False


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")