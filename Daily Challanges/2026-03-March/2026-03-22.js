const ROAST_LEVEL = {
  "'": 1,
  "-": 2,
  ".": 3,
};

function detectRoast(beans) {
  let points = 0;

  for (const bean of beans) {
    points += ROAST_LEVEL[bean];
  }

  const avgPoints = points / beans.length;

  if (avgPoints < 1.75) {
    return "Light";
  } else if (avgPoints <= 2.5) {
    return "Medium";
  } else {
    return "Dark";
  }
}

console.log(detectRoast("''-''''''-'-''--''''"));
console.log(detectRoast(".--.-..-......----.'"));
