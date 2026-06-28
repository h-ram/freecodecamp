symbols = [
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
]

lookup = {s.lower(): s for s in symbols}


def get_periodic_spelling(word):
    w = word.lower()
    memo = {}

    def dfs(i):
        if i == len(w):
            return []
        if i in memo:
            return None
        for l in (2, 1):
            if i + l <= len(w):
                p = w[i : i + l]
                if p in lookup:
                    r = dfs(i + l)
                    if r is not None:
                        return [lookup[p]] + r
        memo[i] = True
        return None

    r = dfs(0)
    return r if r is not None else []


print(get_periodic_spelling("neon"))
print(get_periodic_spelling("rational"))
print(get_periodic_spelling("yarn"))
print(get_periodic_spelling("carbon"))
print(get_periodic_spelling("noisy"))
print(get_periodic_spelling("bicycles"))
print(get_periodic_spelling("optics"))
print(get_periodic_spelling("value"))
