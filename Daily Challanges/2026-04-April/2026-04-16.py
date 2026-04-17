def do_math(s):
    answer = 0
    operand = "0"
    operator = ""
    is_flushed = False
    for char in s:
        if char.isdigit():
            is_flushed = False
            operand += char
        else:
            if not is_flushed:
                is_flushed = True
                if len(operator) % 2 == 0:
                    answer += int(operand)
                else:
                    answer -= int(operand)
                operand = ""
                operator = ""
            operator += char
    operand = int(operand) if operand else 0
    if len(operator) % 2 == 0:
        answer += int(operand)
    else:
        answer -= int(operand)
    return answer


print(do_math("3ab10c8"))
print(do_math("6MINUS4"))
print(
    do_math(
        "a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"
    )
)
