def is_mirror_image(str1, str2) -> bool:
    mirror = {
        # symmetric
        'W': 'W', 'T': 'T', 'Y': 'Y', 'U': 'U',
        'I': 'I', 'O': 'O', 'H': 'H', 'A': 'A',
        'X': 'X', 'V': 'V', 'M': 'M',
        'w': 'w', 'o': 'o', 'x': 'x', 'v': 'v',
        '0': '0', '8': '8',
        '=': '=', '+': '+', ':': ':',
        '|': '|', '-': '-', '_': '_',
        '*': '*', '^': '^', '!': '!',
        '.': '.', ' ': ' ',

        # asymetric
        '[': ']', ']': '[',
        '{': '}', '}': '{',
        '<': '>', '>': '<',
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        '(': ')', ')': '('
    }

    if len(str1) != len(str2):
        return False
    n = len(str1)
    for i in range(n):
        char = str1[i]
        if mirror[char] != str2[n - 1 - i]:
            return False
    return True

print(is_mirror_image("[HOW]", "[WOH]"))
print(is_mirror_image("MOM", "MOM"))