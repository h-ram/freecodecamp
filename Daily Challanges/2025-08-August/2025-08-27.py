def evaluate(numbers, operators):
    result = numbers[0]
    op_index = 0

    for i in range(1, len(numbers)):
        op = operators[op_index]

        if op == '+':
            result += numbers[i]
        elif op == '-':
            result -= numbers[i]
        elif op == '*':
            result *= numbers[i]
        elif op == '/':
            result /= numbers[i]
        elif op == '%':
            result %= numbers[i]

        op_index = (op_index + 1) % len(operators)

    return result

test1 = evaluate([5, 6, 7, 8, 9], ['+', '-'])
test2 = evaluate([17, 61, 40, 24, 38, 14], ['+', '%'])
test3 = evaluate([20, 2, 4, 24, 12, 3], ['*', '/'])
test4 = evaluate([11, 4, 10, 17, 2], ['*', '*', '%'])
test5 = evaluate([33, 11, 29, 13], ['/', '-'])

check1 = 3
check2 = 38
check3 = 60
check4 = 30
check5 = -2

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")