function addPunctuation(sentences) {
  let result = [sentences[0]];

  for (let i = 1; i < sentences.length; i++) {
    if (
      sentences[i] === sentences[i].toUpperCase() &&
      sentences[i - 1] === " "
    ) {
      result[result.length - 1] = ".";
      result.push(" ");
    }

    result.push(sentences[i]);
  }

  result.push(".");
  return result.join("");
}

const test1 = addPunctuation("Hello world");
const test2 = addPunctuation("Hello world It's nice today");
const test3 = addPunctuation("JavaScript is great Sometimes");
const test4 = addPunctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z");
const test5 = addPunctuation("Wait.. For it");

const check1 = "Hello world.";
const check2 = "Hello world. It's nice today.";
const check3 = "JavaScript is great. Sometimes.";
const check4 = "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z.";
const check5 = "Wait... For it.";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);