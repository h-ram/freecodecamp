function truncateText(s) {
  function charWidth(c) {
    if ("ilI".includes(c)) return 1;
    else if ("fjrt".includes(c)) return 2;
    else if ("abcdeghkmnopqrstuvwxyzJL".includes(c)) return 3;
    else if ("ABCDEFGHKMNOPQRSTUVWXYZ".includes(c)) return 4;
    else if (c === " ") return 2;
    else if (c === ".") return 1;
    return 0;
  }

  const total = [...s].reduce((sum, c) => sum + charWidth(c), 0);
  if (total <= 50) {
    return s;
  }

  const maxTextWidth = 47; // 50 - 3 (for "...")
  let running = 0;
  let cutoff = 0;
  for (let i = 0; i < s.length; i++) {
    const w = charWidth(s[i]);
    if (running + w > maxTextWidth) break;
    running += w;
    cutoff = i + 1;
  }

  return s.slice(0, cutoff) + "...";
}

console.log(truncateText("The quick brown fox"));
console.log(truncateText("The fast striped zebra"));
