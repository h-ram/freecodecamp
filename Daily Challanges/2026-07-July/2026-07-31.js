function decodeMorse(code) {
  const morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
  };

  const words = code.split("   ");
  const output = [];

  for (const word of words) {
    let text = "";
    for (const letter of word.split(" ")) {
      text += morse[letter];
    }
    output.push(text);
  }

  return output.join(" ");
}

console.log(decodeMorse("--.."));
console.log(decodeMorse("... --- ..."));
console.log(decodeMorse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."));
console.log(decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."));
console.log(
  decodeMorse(
    "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.",
  ),
);
