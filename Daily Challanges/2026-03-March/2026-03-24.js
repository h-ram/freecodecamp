function passingCount(scores, passingScore) {
  const count = scores.reduce(
    (sum, score) => (score >= passingScore ? sum + 1 : sum + 0),
    0,
  );
  return count;
}

console.log(passingCount([90, 85, 75, 60, 50], 70));
