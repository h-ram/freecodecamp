function getTallyCount(str) {
  return [...str].filter((c) => c === "|" || c === "/").length;
}

console.log(getTallyCount("||||"));
console.log(getTallyCount("||||/"));
console.log(getTallyCount("||||/ |||"));
console.log(getTallyCount("||||/ ||||/ ||||/ ||"));
console.log(getTallyCount("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"));
