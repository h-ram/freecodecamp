function parseFrontmatter(frontmatterString) {
  const parsedData = {};
  const lines = frontmatterString.trim().split("\n");

  for (const line of lines) {
    if (line === "---" || !line.trim()) {
      continue;
    }

    if (line.includes(": ")) {
      const splitIndex = line.indexOf(": ");
      const key = line.slice(0, splitIndex);
      const valueStr = line.slice(splitIndex + 2);

      if (valueStr === "true") {
        parsedData[key] = true;
      } else if (valueStr === "false") {
        parsedData[key] = false;
      } else {
        const num = Number(valueStr);
        if (!isNaN(num) && valueStr.trim() !== "") {
          parsedData[key] = num;
        } else {
          parsedData[key] = valueStr;
        }
      }
    }
  }

  return parsedData;
}

console.log("Test 1:");
const test1 = parseFrontmatter(
  "---\ntitle: My Post\ndraft: false\nviews: 100\n---",
);
console.log(test1);

console.log("\nTest 2:");
const test2 = parseFrontmatter(
  "---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---",
);
console.log(test2);

console.log("\nTest 3:");
const test3 = parseFrontmatter(
  "---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---",
);
console.log(test3);

console.log("\nTest 4:");
const test4 = parseFrontmatter("---\nrating: 4.5\nprice: 9.99\n---");
console.log(test4);
