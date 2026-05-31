function getBestHand(cards) {
  const ranks = cards.map((card) => card[0]);
  const suits = cards.map((card) => card[1]);
  const rankValues = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    T: 10,
    J: 11,
    Q: 12,
    K: 13,
    A: 14,
  };
  const values = ranks.map((r) => rankValues[r]).sort((a, b) => a - b);
  const isFlush = new Set(suits).size === 1;
  let isStraight = false;
  if (new Set(values).size === 5) {
    if (values[4] - values[0] === 4) {
      isStraight = true;
    } else if (
      values.length === 5 &&
      values[0] === 2 &&
      values[1] === 3 &&
      values[2] === 4 &&
      values[3] === 5 &&
      values[4] === 14
    ) {
      isStraight = true;
    }
  }
  const freq = {};
  for (const rank of ranks) {
    freq[rank] = (freq[rank] || 0) + 1;
  }
  const counts = Object.values(freq).sort((a, b) => b - a);
  if (isFlush && ["A", "K", "Q", "J", "T"].every((r) => ranks.includes(r))) {
    return "Royal Flush";
  }

  if (isFlush && isStraight) {
    return "Straight Flush";
  }

  if (counts.length === 2 && counts[0] === 4) {
    return "Four of a Kind";
  }

  if (counts.length === 2 && counts[0] === 3 && counts[1] === 2) {
    return "Full House";
  }

  if (isFlush) {
    return "Flush";
  }

  if (isStraight) {
    return "Straight";
  }

  if (
    counts.length === 3 &&
    counts[0] === 3 &&
    counts[1] === 1 &&
    counts[2] === 1
  ) {
    return "Three of a Kind";
  }

  if (
    counts.length === 3 &&
    counts[0] === 2 &&
    counts[1] === 2 &&
    counts[2] === 1
  ) {
    return "Two Pair";
  }

  if (
    counts.length === 4 &&
    counts[0] === 2 &&
    counts[1] === 1 &&
    counts[2] === 1 &&
    counts[3] === 1
  ) {
    return "Pair";
  }

  return "High Card";
}

console.log(getBestHand(["7s", "7h", "7d", "2c", "5h"]));
console.log(getBestHand(["Ks", "Kh", "Kd", "4s", "4h"]));
console.log(getBestHand(["2h", "5h", "7h", "9h", "Jh"]));
