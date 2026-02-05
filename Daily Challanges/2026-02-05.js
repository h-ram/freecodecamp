function countChange(change) {
    const totalCents = change.reduce((a, b) => a + b, 0);
    const dollars = Math.floor(totalCents / 100);
    const cents = totalCents % 100;
    return `$${dollars}.${cents.toString().padStart(2, '0')}`;
}

const test1 = countChange([25, 10, 5, 1]);
const test2 = countChange([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]);
const test3 = countChange([100, 25, 100, 1000, 5, 500, 2000, 25]);
const test4 = countChange([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]);
const test5 = countChange([1]);
const test6 = countChange([25, 25, 25, 25]);

const check1 = "$0.41";
const check2 = "$1.43";
const check3 = "$37.55";
const check4 = "$0.70";
const check5 = "$0.01";
const check6 = "$1.00";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);