function triageIssue(title, labels) {
  const t = title.toLowerCase();
  labels = [...labels];

  if (labels.length === 0) {
    if (t.includes("error") || t.includes("bug")) {
      labels.push("bug", "needs triage");
    } else if (t.includes("feature") || t.includes("add")) {
      labels.push("enhancement", "discussing");
    }
  } else {
    if (labels.includes("needs triage")) {
      labels = labels.filter((x) => x !== "needs triage");
      if (t.includes("simple") || t.includes("easy")) {
        labels.push("good first issue");
      } else {
        labels.push("help wanted");
      }
    } else if (labels.includes("discussing")) {
      labels = labels.filter((x) => x !== "discussing");
      if (t.includes("planned") || t.includes("next")) {
        labels.push("on the roadmap");
      } else {
        labels.push("help wanted");
      }
    }
  }

  if (t.includes("security") && !labels.includes("critical")) {
    labels.push("critical");
  }

  return labels;
}

console.log(triageIssue("app crashes with error", []));
console.log(triageIssue("app crashes with error", ["bug", "needs triage"]));
console.log(triageIssue("add dark mode", []));
console.log(triageIssue("add dark mode", ["enhancement", "discussing"]));
console.log(triageIssue("xss security bug", []));
console.log(triageIssue("security vulnerability in auth", []));
console.log(triageIssue("easy a11y fix", ["bug", "needs triage"]));
console.log(
  triageIssue("planned api migration", ["enhancement", "discussing"]),
);
console.log(triageIssue("improve security", ["enhancement", "discussing"]));
