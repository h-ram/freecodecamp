def title_case(title):
    return title.title()

test1 = title_case("hello world")
test2 = title_case("the quick brown fox")
test3 = title_case("JAVASCRIPT AND PYTHON")
test4 = title_case("AvOcAdO tOAst fOr brEAkfAst")


check1 = "Hello World"
check2 = "The Quick Brown Fox"
check3 = "Javascript And Python"
check4 = "Avocado Toast For Breakfast"


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")