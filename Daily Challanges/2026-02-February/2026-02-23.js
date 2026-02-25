function canDonate(donor, recipient) {
  const d_letter = donor.slice(0, -1);
  const r_letter = recipient.slice(0, -1);
  const d_sign = donor.slice(-1);
  const r_sign = recipient.slice(-1);

  const valid_donors = {
    O: ["A", "B", "AB", "O"],
    A: ["A", "AB"],
    B: ["B", "AB"],
    AB: ["AB"],
  };

  if (!valid_donors[d_letter].includes(r_letter)) {
    return false;
  }

  if (d_sign + r_sign === "+-") {
    return false;
  }

  return true;
}

const test1 = canDonate("B+", "B+");
const test2 = canDonate("O-", "AB-");
const test3 = canDonate("O+", "A-");
const test4 = canDonate("A+", "AB+");
const test5 = canDonate("A-", "B-");
const test6 = canDonate("B-", "AB+");
const test7 = canDonate("B-", "A+");
const test8 = canDonate("O-", "O+");
const test9 = canDonate("O+", "O-");
const test10 = canDonate("AB+", "AB-");

const check1 = true;
const check2 = true;
const check3 = false;
const check4 = true;
const check5 = false;
const check6 = true;
const check7 = false;
const check8 = true;
const check9 = false;
const check10 = false;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);
console.log(`Test8: ${test8 === check8}`);
console.log(`Test9: ${test9 === check9}`);
console.log(`Test10: ${test10 === check10}`);
