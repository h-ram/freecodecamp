def get_odd_words(s):
    words = s.split(" ")
    return " ".join(word for word in words if len(word) % 2 == 1)


print(get_odd_words("This is a super good test"))
print(get_odd_words("one two three four"))
print(get_odd_words("banana split sundae with rainbow sprinkles on top"))
