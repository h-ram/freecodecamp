function pigLatin(text) {
  const vowels = "aeiou";

  function convert(word) {
    const firstUpper = word[0] === word[0].toUpperCase();
    const lowerWord = word.toLowerCase();
    let result;

    if (vowels.includes(lowerWord[0])) {
      result = lowerWord + "way";
    } else {
      let index = 0;
      while (index < lowerWord.length && !vowels.includes(lowerWord[index])) {
        index++;
      }
      result = lowerWord.slice(index) + lowerWord.slice(0, index) + "ay";
    }

    if (firstUpper) {
      result = result[0].toUpperCase() + result.slice(1);
    }

    return result;
  }

  return text.split(" ").map(convert).join(" ");
}

console.log(pigLatin("universe"));
console.log(pigLatin("hello"));
console.log(pigLatin("hello universe"));
console.log(pigLatin("Hello universe"));
console.log(pigLatin("Pig Latin is fun"));
console.log(pigLatin("The quick brown fox jumped over the lazy dog"));
