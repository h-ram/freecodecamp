function rookBishopAttack(rook, bishop) {
  const [xRook, yRook] = [rook[0].charCodeAt(0), Number(rook[1])];
  const [xBish, yBish] = [bishop[0].charCodeAt(0), Number(bishop[1])];

  if (xRook == xBish || yRook == yBish) return "rook";
  if (Math.abs(xRook - xBish) == Math.abs(yRook - yBish)) return "bishop";
  return "neither";
}

console.log(rookBishopAttack("A1", "A5"));
console.log(rookBishopAttack("C3", "F6"));
console.log(rookBishopAttack("B3", "C5"));
