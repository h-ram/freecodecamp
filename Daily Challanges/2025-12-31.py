import re
def parse_italics(markdown):
    pattern = r'([*_])(?!\s)([^\s](?:.*?[^\s])?)\1'
    return re.sub(pattern, r'<i>\2</i>', markdown) 


test1 = parse_italics("*This is italic*")
test2 = parse_italics("_This is also italic_")
test3 = parse_italics("*This is not italic *")
test4 = parse_italics("_ This is also not italic_")
test5 = parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.")

check1 = "<i>This is italic</i>"
check2 = "<i>This is also italic</i>"
check3 = "*This is not italic *"
check4 = "_ This is also not italic_"
check5 = "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog."


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
