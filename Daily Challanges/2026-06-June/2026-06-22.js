function makeLeet(s) {
  const mp = {
    a: "4",
    e: "3",
    g: "9",
    i: "1",
    l: "1",
    o: "0",
    s: "5",
    t: "7",
  };

  let res = "";
  for (const c of s) {
    res += mp[c] || c;
  }
  return res;
}

console.log(makeLeet("cool"));
console.log(makeLeet("leet"));
console.log(makeLeet("hacker"));
console.log(makeLeet("satellite"));
console.log(makeLeet("abcdefghijklmnopqrstuvwxyz"));
