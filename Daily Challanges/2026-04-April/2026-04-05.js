function getRotation(n) {
  let s = String(n);
  const k = s.length;
  for (let i = 0; i < k; i++) {
    const rotated = Number(s);
    if (rotated % k === 0) {
      return i;
    }
    s = s.slice(1) + s[0];
  }
  return "none";
}
