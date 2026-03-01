function translatePigLatin(str) {
  const vowelRegex = /^[aeiou]/;
  const firstVowelIndex = str.search(/[aeiou]/);

  if (vowelRegex.test(str)) {
    return str + "way";
  }

  if (firstVowelIndex === -1) {
    return str + "ay";
  }

  return str.slice(firstVowelIndex) +
         str.slice(0, firstVowelIndex) +
         "ay";
}

console.log(translatePigLatin("california")) // aliforniacay