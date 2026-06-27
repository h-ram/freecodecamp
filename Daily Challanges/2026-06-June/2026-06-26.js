function triageBlood(inventory, requests) {
  const blood = { O: 0, A: 0, B: 0, AB: 0 };
  const need = { O: 0, A: 0, B: 0, AB: 0 };

  for (const type of inventory) blood[type]++;
  for (const type of requests) need[type]++;

  let served = 0;

  let x = Math.min(blood.O, need.O);
  served += x;
  blood.O -= x;
  need.O -= x;

  x = Math.min(blood.A, need.A);
  served += x;
  blood.A -= x;
  need.A -= x;

  x = Math.min(blood.O, need.A);
  served += x;
  blood.O -= x;
  need.A -= x;

  x = Math.min(blood.B, need.B);
  served += x;
  blood.B -= x;
  need.B -= x;

  x = Math.min(blood.O, need.B);
  served += x;
  blood.O -= x;
  need.B -= x;

  for (const donor of ["AB", "A", "B", "O"]) {
    x = Math.min(blood[donor], need.AB);
    served += x;
    blood[donor] -= x;
    need.AB -= x;
  }

  return `${served} of ${requests.length} patients served`;
}

console.log(triageBlood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]));
console.log(triageBlood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]));
console.log(triageBlood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]));
console.log(triageBlood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]));
console.log(
  triageBlood(
    ["A", "O", "B", "AB", "B", "AB", "O", "A", "A"],
    ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"],
  ),
);
console.log(
  triageBlood(
    [
      "O",
      "B",
      "AB",
      "AB",
      "O",
      "A",
      "A",
      "AB",
      "O",
      "B",
      "B",
      "AB",
      "A",
      "B",
      "AB",
    ],
    ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"],
  ),
);
