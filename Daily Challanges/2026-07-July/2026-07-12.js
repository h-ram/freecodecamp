function horoscopeMatch(sign1, sign2) {
  const signs = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
  ];

  const compatibility = {
    0: "100%",
    1: "40%",
    2: "80%",
    3: "30%",
    4: "90%",
    5: "20%",
    6: "50%",
  };

  const i = signs.indexOf(sign1);
  const j = signs.indexOf(sign2);
  const distance = Math.min(Math.abs(i - j), 12 - Math.abs(i - j));

  return compatibility[distance];
}

console.log(horoscopeMatch("Libra", "Sagittarius"));
console.log(horoscopeMatch("Gemini", "Scorpio"));
console.log(horoscopeMatch("Pisces", "Aries"));
console.log(horoscopeMatch("Capricorn", "Cancer"));
console.log(horoscopeMatch("Aquarius", "Aquarius"));
console.log(horoscopeMatch("Virgo", "Taurus"));
console.log(horoscopeMatch("Leo", "Scorpio"));
