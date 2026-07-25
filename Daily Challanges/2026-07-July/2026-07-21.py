def blend_words(word1, word2):
    first_half = len(word1) // 2
    second_half = len(word2) // 2
    return word1[:first_half] + word2[second_half:]


print(blend_words("turtle", "toucan"))
print(blend_words("chipmunk", "flamingo"))
print(blend_words("falcon", "pelican"))
print(blend_words("hyena", "iguana"))
print(blend_words("scorpion", "gorilla"))
print(blend_words("platypus", "wolverine"))
