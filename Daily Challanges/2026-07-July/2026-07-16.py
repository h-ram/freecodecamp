def pig_latin(text):
    vowels = "aeiou"

    def convert(word):
        first_upper = word[0].isupper()
        lower_word = word.lower()

        if lower_word[0] in vowels:
            result = lower_word + "way"
        else:
            index = 0
            while index < len(lower_word) and lower_word[index] not in vowels:
                index += 1
            result = lower_word[index:] + lower_word[:index] + "ay"

        if first_upper:
            result = result[0].upper() + result[1:]

        return result

    return " ".join(convert(word) for word in text.split())


print(pig_latin("universe"))
print(pig_latin("hello"))
print(pig_latin("hello universe"))
print(pig_latin("Hello universe"))
print(pig_latin("Pig Latin is fun"))
print(pig_latin("The quick brown fox jumped over the lazy dog"))
