def capitalize_fibonacci(s):
    n = len(s)
    fib = set()
    a, b = 0, 1
    while a < n:
        fib.add(a)
        a, b = b, a + b

    res = []
    for i, c in enumerate(s):
        if c.isalpha():
            if i in fib:
                res.append(c.upper())
            else:
                res.append(c.lower())
        else:
            res.append(c)
    return "".join(res)
