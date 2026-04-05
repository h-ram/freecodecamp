def is_valid_equation(equation):
    operand1, operand2 = map(eval, equation.split("="))
    return operand1 == operand2


print(is_valid_equation("2 + 2 = 4"))
