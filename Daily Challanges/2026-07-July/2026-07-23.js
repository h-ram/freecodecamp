function playGame(p1, p2) {
  let score1 = 0;
  let score2 = 0;

  for (let i = 0; i < p1.length; i++) {
    if (p1[i] === "C" && p2[i] === "C") {
      score1 += 3;
      score2 += 3;
    } else if (p1[i] === "D" && p2[i] === "D") {
      score1 += 1;
      score2 += 1;
    } else if (p1[i] === "D") {
      score1 += 5;
    } else {
      score2 += 5;
    }
  }

  return [score1, score2];
}

console.log(playGame("CCCC", "CCCC"));
console.log(playGame("DDDD", "DDDD"));
console.log(playGame("CCDD", "CDDD"));
console.log(playGame("CCCDCDCCCDDC", "CCDDCDCDDCCD"));
console.log(playGame("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"));
