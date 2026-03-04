def sum_letters(s):
    letters = [letter for letter in s.lower() if letter.isalpha()]
    values = [ord(letter) - 96 for letter in letters]
    return sum(values)

test1 = sum_letters("Hello")
test2 = sum_letters("freeCodeCamp")
test3 = sum_letters("The quick brown fox jumps over the lazy dog.")
test4 = sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.")
test5 = sum_letters("</404>")

check1 = 52
check2 = 94
check3 = 473
check4 = 1681
check5 = 0

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")