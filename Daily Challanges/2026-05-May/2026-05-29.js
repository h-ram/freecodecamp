function getWiderAspectRatio(dim1, dim2) {
  const [w1, h1] = dim1.split("x").map(Number);
  const [w2, h2] = dim2.split("x").map(Number);

  let w, h;

  if (w1 * h2 >= w2 * h1) {
    w = w1;
    h = h1;
  } else {
    w = w2;
    h = h2;
  }

  const gcd = (a, b) => {
    while (b !== 0) {
      [a, b] = [b, a % b];
    }
    return a;
  };

  const g = gcd(w, h);
  return `${w / g}:${h / g}`;
}

console.log(getWiderAspectRatio("1920x1080", "800x600"));
console.log(getWiderAspectRatio("1080x1350", "2048x1536"));
console.log(getWiderAspectRatio("640x480", "2440x1220"));
