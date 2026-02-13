def repeat_vowels(s):

    vowels = ['a','e','i','o','u']
    result = ""

    factor = 0
    for char in s:
        if char.lower() in vowels:
            result += char
            result += char.lower() * factor
            factor +=1
        else:
            result += char
            
    return result

test1 = repeat_vowels("hello world")
test2 = repeat_vowels("freeCodeCamp")
test3 = repeat_vowels("AEIOU")
test4 = repeat_vowels("I like eating ice cream in Iceland")

check1 = "helloo wooorld"
check2 = "freeeCooodeeeeCaaaaamp"
check3 = "AEeIiiOoooUuuuu"
check4 = "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")