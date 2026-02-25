function scoreCurling(house) {
  let red = [];
  let yellow = [];

  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (house[i][j] === "R") {
        red.push(Math.max(Math.abs(i - 2), Math.abs(j - 2)));
      } else if (house[i][j] === "Y") {
        yellow.push(Math.max(Math.abs(i - 2), Math.abs(j - 2)));
      }
    }
  }

  if (red.length === 0 && yellow.length === 0) {
    return "No points awarded";
  }

  if (red.length === 0) {
    return `Y: ${yellow.length}`;
  }

  if (yellow.length === 0) {
    return `R: ${red.length}`;
  }

  const closestRed = Math.min(...red);
  const closestYellow = Math.min(...yellow);

  if (closestRed === closestYellow) {
    return "No points awarded";
  }

  if (closestRed < closestYellow) {
    const points = red.filter((r) => r < closestYellow).length;
    return `R: ${points}`;
  } else {
    const points = yellow.filter((r) => r < closestRed).length;
    return `Y: ${points}`;
  }
}

const test1 = scoreCurling([
  [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", "R", ".", ".", "."],
  [".", ".", ".", ".", "."],
]);
const test2 = scoreCurling([
  [".", ".", "R", ".", "."],
  [".", ".", ".", ".", "."],
  [".", ".", "Y", ".", "R"],
  [".", ".", "Y", "Y", "."],
  [".", "Y", "R", "R", "."],
]);
const test3 = scoreCurling([
  [".", "R", "Y", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", ".", ".", ".", "."],
  [".", "Y", "R", "Y", "."],
  [".", ".", "R", "R", "."],
]);
const test4 = scoreCurling([
  [".", "Y", "Y", ".", "."],
  ["Y", ".", ".", "R", "."],
  [".", ".", "R", ".", "."],
  [".", ".", "R", "R", "."],
  [".", "Y", "R", "Y", "."],
]);
const test5 = scoreCurling([
  ["Y", "Y", "Y", "Y", "Y"],
  ["Y", "R", "R", "R", "Y"],
  ["Y", "R", "Y", "R", "Y"],
  ["Y", "R", "R", "R", "Y"],
  ["Y", "Y", "Y", "Y", "Y"],
]);
const test6 = scoreCurling([
  ["Y", "R", "Y", "R", "Y"],
  ["R", ".", ".", ".", "R"],
  ["Y", ".", ".", ".", "Y"],
  ["R", ".", ".", ".", "R"],
  ["Y", ".", ".", "R", "Y"],
]);

const check1 = "R: 2";
const check2 = "Y: 3";
const check3 = "No points awarded";
const check4 = "R: 4";
const check5 = "Y: 1";
const check6 = "No points awarded";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
