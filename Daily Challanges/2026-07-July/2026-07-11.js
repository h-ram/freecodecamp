function fiveDice(dice) {
  const counts = Object.values(
    dice.reduce((m, x) => {
      m[x] = (m[x] || 0) + 1;
      return m;
    }, {}),
  ).sort((a, b) => b - a);

  const s = [...new Set(dice)].sort((a, b) => a - b);

  if (counts.join() === "5") return "five of a kind";
  if (counts.join() === "4,1") return "four of a kind";
  if (s.join() === "1,2,3,4,5" || s.join() === "2,3,4,5,6")
    return "large straight";
  if (counts.join() === "3,2") return "full house";

  let small = false;
  for (let i = 0; i <= s.length - 4; i++) {
    if (s.slice(i, i + 4).every((v, j) => v === s[i] + j)) {
      small = true;
      break;
    }
  }
  if (small) return "small straight";
  if (counts.join() === "3,1,1") return "three of a kind";
  if (counts.join() === "2,2,1") return "two pair";
  if (counts.join() === "2,1,1,1") return "pair";
  return "no pair";
}

console.log(fiveDice([1, 1, 1, 1, 1]));
console.log(fiveDice([5, 5, 5, 6, 5]));
console.log(fiveDice([2, 5, 6, 4, 3]));
console.log(fiveDice([4, 3, 3, 3, 1]));
console.log(fiveDice([4, 6, 2, 6, 5]));
console.log(fiveDice([1, 4, 5, 6, 2]));
console.log(fiveDice([1, 3, 4, 6, 2]));
console.log(fiveDice([2, 2, 5, 2, 5]));
console.log(fiveDice([6, 4, 5, 6, 4]));
