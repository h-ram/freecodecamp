def to_snake(camel):
    snake = ""

    for letter in camel:
        if letter.isupper():
            snake += '_' + letter.lower()
        else:
            snake += letter
    return snake

test1 = to_snake("helloWorld")
test2 = to_snake("myVariableName")
test3 = to_snake("freecodecampDailyChallenges")

check1 = "hello_world"
check2 = "my_variable_name"
check3 = "freecodecamp_daily_challenges"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")