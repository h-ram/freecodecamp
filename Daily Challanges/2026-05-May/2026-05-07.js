function getLongestSubstring(s) {
  const n = s.length;
  let windowSize = n - 1;
  let memory = new Set();
  while (windowSize > 0) {
    for (let i = 0; i < n - windowSize + 1; i++) {
      const window = s.slice(i, i + windowSize);
      if (memory.has(window)) {
        return window;
      }
      memory.add(window);
    }
    windowSize--;
    memory = new Set();
  }
  return s;
}

console.log(getLongestSubstring("abracadabra"));
console.log(getLongestSubstring("hello world hello"));
