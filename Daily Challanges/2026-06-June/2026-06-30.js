function duplicateCharacterCount(str1, str2) {
  const chars = new Set(str1);
  let count = 0;
  for (const c of str2) {
    if (chars.has(c)) count++;
  }
  return count;
}

console.log(duplicateCharacterCount("aloha", "hei"));
console.log(duplicateCharacterCount("jambo", "bonjour"));
