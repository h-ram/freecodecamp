function getOpenIssues(issues, prs) {
  function rotations(s) {
    const result = new Set();
    for (let i = 0; i < s.length; i++) {
      result.add(s.slice(i) + s.slice(0, i));
    }
    return result;
  }
  function closes(issue, pr) {
    let a = String(issue);
    let b = String(pr);
    const n = Math.max(a.length, b.length);

    a = a.padStart(n, "0");
    b = b.padStart(n, "0");

    if (a === b) return false;
    return rotations(a).has(b);
  }
  const openIssues = [];
  for (const issue of issues) {
    let closed = false;

    for (const pr of prs) {
      if (closes(issue, pr)) {
        closed = true;
        break;
      }
    }
    if (!closed) openIssues.push(issue);
  }
  return openIssues;
}

console.log(getOpenIssues([123, 234], [231]));
console.log(getOpenIssues([123, 345, 16], [345, 231]));
