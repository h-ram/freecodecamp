const symbols = [
  "H",
  "He",
  "Li",
  "Be",
  "B",
  "C",
  "N",
  "O",
  "F",
  "Ne",
  "Na",
  "Mg",
  "Al",
  "Si",
  "P",
  "S",
  "Cl",
  "Ar",
  "K",
  "Ca",
  "Sc",
  "Ti",
  "V",
  "Cr",
  "Mn",
  "Fe",
  "Co",
  "Ni",
  "Cu",
  "Zn",
  "Ga",
  "Ge",
  "As",
  "Se",
  "Br",
  "Kr",
  "Rb",
  "Sr",
  "Y",
  "Zr",
  "Nb",
  "Mo",
  "Tc",
  "Ru",
  "Rh",
  "Pd",
  "Ag",
  "Cd",
  "In",
  "Sn",
  "Sb",
  "Te",
  "I",
  "Xe",
  "Cs",
  "Ba",
  "La",
  "Ce",
  "Pr",
  "Nd",
  "Pm",
  "Sm",
  "Eu",
  "Gd",
  "Tb",
  "Dy",
  "Ho",
  "Er",
  "Tm",
  "Yb",
  "Lu",
  "Hf",
  "Ta",
  "W",
  "Re",
  "Os",
  "Ir",
  "Pt",
  "Au",
  "Hg",
  "Tl",
  "Pb",
  "Bi",
  "Po",
  "At",
  "Rn",
  "Fr",
  "Ra",
  "Ac",
  "Th",
  "Pa",
  "U",
  "Np",
  "Pu",
  "Am",
  "Cm",
  "Bk",
  "Cf",
  "Es",
  "Fm",
  "Md",
  "No",
  "Lr",
  "Rf",
  "Db",
  "Sg",
  "Bh",
  "Hs",
  "Mt",
  "Ds",
  "Rg",
  "Cn",
  "Nh",
  "Fl",
  "Mc",
  "Lv",
  "Ts",
  "Og",
];

const lookup = {};
for (const symbol of symbols) {
  lookup[symbol.toLowerCase()] = symbol;
}

function getPeriodicSpelling(word) {
  word = word.toLowerCase();
  const memo = {};

  function dfs(index) {
    if (index === word.length) return [];
    if (index in memo) return null;

    for (const len of [2, 1]) {
      if (index + len <= word.length) {
        const part = word.slice(index, index + len);
        if (part in lookup) {
          const result = dfs(index + len);
          if (result !== null) {
            return [lookup[part], ...result];
          }
        }
      }
    }

    memo[index] = true;
    return null;
  }

  const result = dfs(0);
  return result !== null ? result : [];
}

console.log(getPeriodicSpelling("neon"));
console.log(getPeriodicSpelling("rational"));
console.log(getPeriodicSpelling("yarn"));
console.log(getPeriodicSpelling("carbon"));
console.log(getPeriodicSpelling("noisy"));
console.log(getPeriodicSpelling("bicycles"));
console.log(getPeriodicSpelling("optics"));
console.log(getPeriodicSpelling("value"));
