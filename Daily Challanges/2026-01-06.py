def vowel_case(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    converted = [letter.upper() if letter.lower() in vowels else letter.lower() for letter in s]
    
    return "".join(converted)


test1 = vowel_case("vowelcase")
test2 = vowel_case("coding is fun")
test3 = vowel_case("HELLO, world!")
test4 = vowel_case("git cherry-pick")
test5 = vowel_case("HEAD~1")


check1 = "vOwElcAsE"
check2 = "cOdIng Is fUn"
check3 = "hEllO, wOrld!"
check4 = "gIt chErry-pIck"
check5 = "hEAd~1"


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
