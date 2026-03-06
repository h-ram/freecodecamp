function navigateTrail(map) {
  let path = "";
  let m = map.length;
  let n = map[0].length;

  let startingCoords = [0, 0];
  let found = false;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (map[i][j] == "C") {
        startingCoords = [i, j];
        found = true;
        break;
      }
    }
    if (found) {
      break;
    }
  }

  let coords = [...startingCoords];
  while (true) {
    const [x, y] = coords;
    map[x] = map[x].substring(0, y) + "V" + map[x].substring(y + 1);

    if (x > 0 && (map[x - 1][y] === "T" || map[x - 1][y] === "G")) {
      coords = [x - 1, y];
      path += "U";
    } else if (y < n - 1 && (map[x][y + 1] === "T" || map[x][y + 1] === "G")) {
      coords = [x, y + 1];
      path += "R";
    } else if (x < m - 1 && (map[x + 1][y] === "T" || map[x + 1][y] === "G")) {
      coords = [x + 1, y];
      path += "D";
    } else if (y > 0 && (map[x][y - 1] === "T" || map[x][y - 1] === "G")) {
      coords = [x, y - 1];
      path += "L";
    } else {
      break;
    }

    if (map[coords[0]][coords[1]] === "G") {
      break;
    }
  }
  return path;
}

const test1 = navigateTrail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]);
const test2 = navigateTrail(["-----", "--TTG", "--T--", "--T--", "CTT--"]);
const test3 = navigateTrail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]);
const test4 = navigateTrail([
  "--------",
  "-CTTT---",
  "----T---",
  "---GT---",
  "--------",
]);
const test5 = navigateTrail([
  "TTTTTTT-",
  "T-----T-",
  "T-----T-",
  "TTTT--TG",
  "---C----",
]);

const check1 = "RDDRDD";
const check2 = "RRUUURR";
const check3 = "DLDDRRRRD";
const check4 = "RRRDDL";
const check5 = "ULLLUUURRRRRRDDDR";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
