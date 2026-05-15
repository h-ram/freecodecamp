function isMirrorImage(str1, str2) {
  const mirror = {
    // symmetric
    W: "W",
    T: "T",
    Y: "Y",
    U: "U",
    I: "I",
    O: "O",
    H: "H",
    A: "A",
    X: "X",
    V: "V",
    M: "M",
    w: "w",
    o: "o",
    x: "x",
    v: "v",
    0: "0",
    8: "8",
    "=": "=",
    "+": "+",
    ":": ":",
    "|": "|",
    "-": "-",
    _: "_",
    "*": "*",
    "^": "^",
    "!": "!",
    ".": ".",
    " ": " ",

    // asymmetric
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    b: "d",
    d: "b",
    p: "q",
    q: "p",
    "(": ")",
    ")": "(",
  };

  if (str1.length !== str2.length) return false;
  const n = str1.length;
  for (let i = 0; i < n; i++) {
    const char = str1[i];
    if (mirror[char] !== str2[n - 1 - i]) return false;
  }
  return true;
}

console.log(isMirrorImage("[HOW]", "[WOH]")); // true
console.log(isMirrorImage("MOM", "MOM")); // true
