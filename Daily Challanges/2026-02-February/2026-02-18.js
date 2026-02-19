function calculateStartDelays(jumpScores) {
    const bestScore = Math.max(...jumpScores);
    const delays = jumpScores.map(score =>
        Math.ceil((bestScore - score) * 1.5)
    );
    return delays;
}


const test1 = calculateStartDelays([120, 110, 125]);
const test2 = calculateStartDelays([118, 125, 122, 120]);
const test3 = calculateStartDelays([100, 105, 95, 110, 120, 115, 108]);
const test4 = calculateStartDelays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]);

const check1 = [8, 23, 0];
const check2 = [11, 0, 5, 8];
const check3 = [30, 23, 38, 15, 0, 8, 18];
const check4 = [3, 11, 6, 18, 21, 15, 8, 26, 0, 12];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);