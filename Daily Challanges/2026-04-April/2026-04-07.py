def palindrome_locator(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return "none"
    if n%2==0:
        return s[n//2-1] + s[n//2]
    else:
        return s[n//2]

print(palindrome_locator("racecar"))
print(palindrome_locator("level"))
print(palindrome_locator("freecodecamp"))