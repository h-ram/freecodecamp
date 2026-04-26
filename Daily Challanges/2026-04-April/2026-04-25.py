def decompress(s):
    mapper = {}
    decompressed = []
    for i, word in enumerate(s.split(" ")):
        if word.isdigit():
            decompressed.append(mapper[word])
        else:
            mapper[str(i + 1)] = word
            decompressed.append(word)
    return " ".join(decompressed)


print(decompress("practice makes perfect and 3 1 2 3"))
