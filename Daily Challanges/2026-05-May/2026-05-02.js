function getDeepestBrackets(s) {
  let maxDepth = 0;
  let depth = 0;
  let deepestWord = [];

  for (let char of s) {
    if ("({[".includes(char)) {
      depth++;
      if (depth > maxDepth) {
        maxDepth = depth;
        deepestWord = [];
      }
    } else if (")}]".includes(char)) {
      depth--;
    } else {
      if (depth === maxDepth) {
        deepestWord.push(char);
      }
    }
  }

  return deepestWord.join("");
}

console.log(getDeepestBrackets("(hello (world))"));
console.log(getDeepestBrackets("[outer [inner] outer]"));
console.log(getDeepestBrackets("{a{b}c{d{e}f}g}"));
console.log(
  getDeepestBrackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"),
);
console.log(getDeepestBrackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"));
