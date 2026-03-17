const STARTING_POINTS = 8 * 1 + 5 * 2 + 3 * 2 + 3 * 2 + 9 * 1;
const PIECE_POINTS = {
  K: 0,
  P: 1,
  N: 3,
  B: 3,
  R: 5,
  Q: 9,
};

function getCapturedValue(pieces) {
  if (!pieces.includes("K")) {
    return "Checkmate";
  }
  let current_points = pieces.reduce(
    (sum, piece) => sum + PIECE_POINTS[piece],
    0,
  );

  return STARTING_POINTS - current_points;
}
console.log(
  getCapturedValue([
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "R",
    "R",
    "N",
    "B",
    "Q",
    "K",
  ]),
);
