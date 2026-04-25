def compress(s):
    found = {}
    compressed = []
    for i, word in enumerate(s.split(' ')):
        if word in found:
            compressed.append(found[word])
        else:
            found[word] = str(i+1)
            compressed.append(word)
    return ' '.join(compressed)


print(compress("practice makes perfect and perfect practice makes perfect"))
print(compress("hello hello hello"))