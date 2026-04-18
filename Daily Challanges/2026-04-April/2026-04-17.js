function decode(message) {
  const KEY = "VLHCGMDLNH";
  let decoded = [];
  let keyIndex = 0;

  for (let i = 0; i < message.length; i++) {
    let char = message[i];

    if (/[A-Z]/.test(char)) {
      let shiftSize =
        KEY.charCodeAt(keyIndex % KEY.length) - "A".charCodeAt(0) + 1;

      // In JS, % can return negative numbers, so we add 26 before the final modulo
      let charCode = char.charCodeAt(0) - "A".charCodeAt(0);
      let decodedVal = (charCode - shiftSize) % 26;
      if (decodedVal < 0) decodedVal += 26;

      decoded.push(String.fromCharCode(decodedVal + "A".charCodeAt(0)));
      keyIndex++;
    } else {
      decoded.push(char);
    }
  }

  return decoded.join("");
}

console.log(decode("YAVJYNXE"));
console.log(decode("YALLUT PQUMJP"));
console.log(decode("UAC DYR EISAKYM"));
console.log(decode("GQMS NBMZU"));
console.log(decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"));
