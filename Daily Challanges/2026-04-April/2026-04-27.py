def get_word_score(word):
    total = sum(ord(char.lower()) - ord("a") + 1 for char in word)
    return total


print(get_word_score("hi"))
print(get_word_score("hello"))
print(get_word_score("hippopotamus"))
