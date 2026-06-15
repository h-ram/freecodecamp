function isValidCard(cardNumber) {
  let total = 0;
  for (let i = 0; i < cardNumber.length; i++) {
    let digit = parseInt(cardNumber[cardNumber.length - 1 - i], 10);
    if (i % 2 === 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    total += digit;
  }
  return total % 10 === 0;
}

console.log(isValidCard("4532015112830366"));
console.log(isValidCard("5425233430109903"));
console.log(isValidCard("371449635398431"));
console.log(isValidCard("6011111111111117"));
console.log(isValidCard("4532015112830367"));
console.log(isValidCard("1234567890123456"));
console.log(isValidCard("4532015112830368"));
