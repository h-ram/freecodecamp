def get_lucky_number(name):
    first, last = name.split()
    def counts(s):
        vowels = sum(c.lower() in "aeiou" for c in s)
        consonants = sum(c.isalpha() and c.lower() not in "aeiou" for c in s)
        return vowels, consonants, len(s)

    v1, c1, l1 = counts(first)
    v2, c2, l2 = counts(last)

    small = min(v1, v2) * min(c1, c2) * min(l1, l2)
    large = max(v1, v2) * max(c1, c2) * max(l1, l2)

    ans = large - small
    return 13 if ans == 0 else ans


print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))