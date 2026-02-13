def parse_inline_code(markdown):
    html = []
    in_code = False

    for ch in markdown:
        if ch == '`':
            if in_code:
                html.append("</code>")
            else:
                html.append("<code>")
            in_code = not in_code
        else:
            html.append(ch)

    return "".join(html)


test1 = parse_inline_code("Use `let` to declare the variable.")
test2 = parse_inline_code("Use `let` or `const` to declare a variable.")
test3 = parse_inline_code("Run `npm install` then `npm start`.")

check1 = "Use <code>let</code> to declare the variable."
check2 = "Use <code>let</code> or <code>const</code> to declare a variable."
check3 = "Run <code>npm install</code> then <code>npm start</code>."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
