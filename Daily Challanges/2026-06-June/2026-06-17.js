function cast(spells) {
  const score = {
    f: [3, "D"],
    l: [3, "D"],
    i: [2, "C"],
    w: [2, "C"],
    h: [1, "R"],
    s: [1, "R"],
  };

  let total = 0;
  let multiplier = 1;
  let prevCategory = null;

  for (const spell of spells) {
    const [base, category] = score[spell];

    if (prevCategory !== null) {
      if (category !== prevCategory) {
        multiplier++;
      } else {
        multiplier = 1;
      }
    }

    total += base * multiplier;
    prevCategory = category;
  }

  return total;
}

console.log(cast("fihwl"));
console.log(cast("lwswfi"));
console.log(cast("wislhfl"));
console.log(cast("sihwlih"));
console.log(cast("wishlfihwslwifihl"));
