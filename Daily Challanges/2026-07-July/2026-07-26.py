def letter_distance(s1, s2):
    total = 0

    for i in range(len(s1)):
        diff = abs(ord(s1[i]) - ord(s2[i]))
        total += min(diff, 26 - diff)

    return total


print(letter_distance("abc", "bcd"))
print(letter_distance("abc", "xyz"))
print(letter_distance("encrypt", "decrypt"))
print(letter_distance("algorithm", "codeblock"))
print(letter_distance("lobster", "penguin"))
print(letter_distance("alligator", "crocodile"))