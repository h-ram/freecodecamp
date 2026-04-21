const DICT = {
  NASA: "National Avocado Storage Authority",
  CIA: "Cats Infiltration Agency",
  FBI: "Fluffy Beanbag Inspectors",
  DOJ: "Department Of Jelly",
  WHO: "Wild Honey Organization",
  EPA: "Eating Pancakes Administration",
};

function findOrg(acronym) {
  return DICT[acronym];
}

console.log(findOrg("NASA"));
console.log(findOrg("CIA"));
console.log(findOrg("FBI"));
