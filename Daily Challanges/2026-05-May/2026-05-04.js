function convertParsecs(parsecs) {
  return parsecs * (parsecs % 2 ? 2 : 3);
}

console.log(convertParsecs(1));
console.log(convertParsecs(2));
