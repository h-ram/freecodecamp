def jbelmu(text):
    result = []
    words = text.split(' ')
    for word in words:
        if len(word) < 4:
            result.append(word)
            continue

        middle = word[1:-1]
        sorted_middle = ''.join(sorted(middle))
        result.append(word[0] + sorted_middle + word[-1])

    result = ' '.join(result)
    return result


test1 = jbelmu("hello world")
test2 = jbelmu("i love jumbled text")
test3 = jbelmu("freecodecamp is my favorite place to learn to code")
test4 = jbelmu("the quick brown fox jumps over the lazy dog")

check1 = "hello wlord"
check2 = "i love jbelmud text"
check3 = "faccdeeemorp is my faiortve pacle to laern to cdoe" 
check4 = "the qciuk borwn fox jmpus oevr the lazy dog"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")