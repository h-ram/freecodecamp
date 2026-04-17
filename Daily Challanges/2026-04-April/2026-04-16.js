function doMath(str) {
  let answer = 0
  let operand = ''
  let operator = ''
  let is_flushed = false
  for(const char of str){
    if(/^[0-9]$/.test(char)){
      is_flushed = false
      operand += char
    }else{
      if(! is_flushed){
        is_flushed = true
        if(operator.length %2 == 0) answer += Number(operand)
        else answer -= Number(operand)
        operand = ''
        operator = ''
      }
      operator += char
    }
  }
  if(operator.length %2 == 0) answer += Number(operand)
  else answer -= Number(operand)
  return answer;
}

console.log(doMath("3ab10c8"))
console.log(doMath("6MINUS4"))
console.log(doMath("9plus3"))