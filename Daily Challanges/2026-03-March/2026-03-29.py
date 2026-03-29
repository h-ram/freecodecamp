def is_valid_isbn10(s):
    s = s.replace("-", "")
    if len(s) != 10:
        return False
    total = 0
    for i in range(10):
        if i < 9:
            if not s[i].isdigit():
                return False
            value = int(s[i])
        else:
            if s[i] == "X":
                value = 10
            elif s[i].isdigit():
                value = int(s[i])
            else:
                return False
        total += value * (i + 1)
    return total % 11 == 0
