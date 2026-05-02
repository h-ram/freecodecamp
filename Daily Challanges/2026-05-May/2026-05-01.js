function groupAnagrams(words) {
  const groups = {};
  for (const word of words) {
    const count = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
      count[word.charCodeAt(i) - 97]++;
    }
    const key = count.join("#");
    if (!groups[key]) {
      groups[key] = [];
    }
    groups[key].push(word);
  }
  return Object.values(groups);
}
console.log(groupAnagrams(["listen", "silent", "hello", "enlist", "world"]));
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
