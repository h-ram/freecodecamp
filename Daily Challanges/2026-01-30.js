function findPawnMoves(position) {
  let moves = [];
  const col = position[0];
  const row = Number(position[1]);

  // at the last row
  if (row == 8) {
    return moves;
  }

  moves.push(`${col}${row + 1}`);

  // first move (double jump allowed)
  if (row == 2) {
    moves.push(col + "4");
  }

  console.log(position, moves);
  return moves;
}

const test1 = findPawnMoves("D4");
const test2 = findPawnMoves("B2");
const test3 = findPawnMoves("A7");
const test4 = findPawnMoves("G2");
const test5 = findPawnMoves("E3");

const check1 = ["D5"];
const check2 = ["B3", "B4"];
const check3 = ["A8"];
const check4 = ["G3", "G4"];
const check5 = ["E4"];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);
