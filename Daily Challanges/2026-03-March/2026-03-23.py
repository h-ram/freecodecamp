def has_no_repeats(s):
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return False
    return True

print(has_no_repeats("hi world"))