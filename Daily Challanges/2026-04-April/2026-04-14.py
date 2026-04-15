def get_last_letter(s):
    last = "!"
    for char in s:
        if char.lower() > last.lower():
            last = char
    return last


print(get_last_letter("world"))
print(get_last_letter("Hello World"))
print(get_last_letter("The quick brown fox jumped over the lazy dog."))
print(get_last_letter("HeLl0"))
print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))
