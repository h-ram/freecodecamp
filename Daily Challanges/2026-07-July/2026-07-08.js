function triageIssue(milliseconds, lastMessage) {
  if (milliseconds < 604800000) return "leave it";
  if (lastMessage.toLowerCase().includes("bump")) return "close it";
  return "bump it";
}

console.log(triageIssue(86400000, "Lets fix it"));
console.log(triageIssue(1209600000, "still waiting"));
console.log(triageIssue(864000000, "bump"));
console.log(triageIssue(604800000, "Do we still want this?"));
console.log(triageIssue(604800000, "Bumping this"));
console.log(triageIssue(345600000, "I'll make a PR"));
