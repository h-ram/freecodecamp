def get_bingo_range(letter):
    if letter == "B":
        return list(range(1, 16))
    elif letter == "I":
        return list(range(16, 31))
    elif letter == "N":
        return list(range(31, 46))
    elif letter == "G":
        return list(range(46, 61))
    else:
        return list(range(61, 76))


print(get_bingo_range("B"))
print(get_bingo_range("I"))
print(get_bingo_range("N"))
print(get_bingo_range("G"))
print(get_bingo_range("O"))
