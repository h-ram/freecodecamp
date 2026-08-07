function getContrastRating(light, dark, large) {
  function luminance(rgb) {
    const values = [];

    for (let channel of rgb) {
      channel /= 255;

      if (channel <= 0.04045) {
        channel /= 12.92;
      } else {
        channel = Math.pow((channel + 0.055) / 1.055, 2.4);
      }

      values.push(channel);
    }

    return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2];
  }

  const ratio = (luminance(light) + 0.05) / (luminance(dark) + 0.05);

  if (large) {
    if (ratio >= 4.5) {
      return "AAA";
    }
    if (ratio >= 3) {
      return "AA";
    }
  } else {
    if (ratio >= 7) {
      return "AAA";
    }
    if (ratio >= 4.5) {
      return "AA";
    }
  }

  return "Fail";
}

console.log(getContrastRating([255, 255, 255], [0, 0, 0], false));
console.log(getContrastRating([215, 188, 188], [55, 55, 55], false));
console.log(getContrastRating([143, 144, 210], [46, 47, 61], false));
console.log(getContrastRating([167, 167, 210], [53, 10, 53], true));
console.log(getContrastRating([135, 147, 155], [60, 70, 90], true));
console.log(getContrastRating([125, 210, 195], [105, 130, 90], true));
