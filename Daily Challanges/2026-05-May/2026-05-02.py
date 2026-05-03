def get_deepest_brackets(s):
    max_depth = 0
    depth = 0
    deepest_word = []
    for char in s:
        if char in '({[':
            depth += 1
            if depth > max_depth:
                max_depth = depth
                deepest_word = []
        elif char in ')}]':
            depth -= 1
        else:
            if depth == max_depth:
                deepest_word.append(char)
    return ''.join(deepest_word)

print(get_deepest_brackets("(hello (world))"))
print(get_deepest_brackets("[outer [inner] outer]"))
print(get_deepest_brackets("{a{b}c{d{e}f}g}"))
print(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"))
print(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"))