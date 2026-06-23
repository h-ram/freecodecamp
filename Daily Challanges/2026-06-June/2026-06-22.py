def make_leet(s):
    mp = {
        "a": "4",
        "e": "3",
        "g": "9",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7",
    }
    res = ""
    for c in s:
        res += mp.get(c, c)
    return res


print(make_leet("cool"))
print(make_leet("leet"))
print(make_leet("hacker"))
print(make_leet("satellite"))
print(make_leet("abcdefghijklmnopqrstuvwxyz"))
