function cardValues(cards) {
  let numericValues = [];
  cards.forEach((card) => {
    const value = card.slice(0, -1);

    if (["J", "Q", "K"].includes(value)) {
      numericValues.push(10);
    } else if (value === "A") {
      numericValues.push(1);
    } else {
      numericValues.push(Number(value));
    }
  });
  return numericValues;
}

const test1 = cardValues(["3H", "4D", "5S"]);
const test2 = cardValues(["AS", "10S", "10H", "6D", "7D"]);
const test3 = cardValues(["8D", "QS", "2H", "JC", "9C"]);
const test4 = cardValues(["AS", "KS"]);
const test5 = cardValues(["10H", "JH", "QH", "KH", "AH"]);

const check1 = [3, 4, 5];
const check2 = [1, 10, 10, 6, 7];
const check3 = [8, 10, 2, 10, 9];
const check4 = [1, 10];
const check5 = [10, 10, 10, 10, 1];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);
