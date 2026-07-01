def duplicate_character_count(str1, str2):
    str1_set = set(str1)
    dup_count = 0
    for letter in str2:
        if letter in str1_set:
            dup_count += 1
    return dup_count

print(duplicate_character_count("aloha", "hei"))
print(duplicate_character_count("jambo", "bonjour"))
print(duplicate_character_count("hello", "hola"))