def decode(s):
    stack = []

    for c in s:
        if c == ')':
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop() 
            stack.extend(temp)  
        else:
            stack.append(c)

    return ''.join(stack)
    return s


test1 = decode("(f(b(dc)e)a)")
test2 = decode("((is?)(a(t d)h)e(n y( uo)r)aC)")
test3 = decode("f(Ce(re))o((e(aC)m)d)p")

check1 = "abcdef"
check2 = "Can you read this?"
check3 = "freeCodeCamp"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")