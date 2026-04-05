function isValidEquation(equation) {
  const [op1, op2] = equation.split("=").map((op) => eval(op));
  return op1 === op2;
}

console.log(isValidEquation("2 + 2 = 4"));
