def get_rotation(n):
    s = str(n)
    k = len(s)
    for i in range(k):
        rotated = int(s)
        if rotated % k == 0:
            return i
        s = s[1:] + s[0]
    return "none"


print(get_rotation(123))
