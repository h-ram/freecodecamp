def decode(message, shift):
    result = []

    for ch in message:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)

    return "".join(result)


test1 = decode("Xlmw mw e wigvix qiwweki.", 4)
test2 = decode("Byffi Qilfx!", 20)
test3 = decode("Zqd xnt njzx?", -1)
test4 = decode("oannLxmnLjvy", 9)

check1 = "This is a secret message."
check2 = "Hello World!"
check3 = "Are you okay?"
check4 = "freeCodeCamp"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")