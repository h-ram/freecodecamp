function parseUrlQuery(url) {
  const queryString = url.split("?")[1];
  const pairs = queryString.split("&");
  let dictionary = {};
  for (const pair of pairs) {
    const [key, value] = pair.split("=");
    dictionary[key] = value;
  }
  return dictionary;
}

console.log(parseUrlQuery("https://example.com/search?name=Alice&age=30"));
console.log(
  parseUrlQuery(
    "https://freecodecamp.org/learn?skill=programming&language=python",
  ),
);
