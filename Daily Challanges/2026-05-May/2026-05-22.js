function getMeetingTime(availability) {
  let common = [[0, 24]];
  for (let person of availability) {
    let newCommon = [];
    for (let [cStart, cEnd] of common) {
      for (let [pStart, pEnd] of person) {
        let start = Math.max(cStart, pStart);
        let end = Math.min(cEnd, pEnd);
        if (end - start >= 1) {
          newCommon.push([start, end]);
        }
      }
    }
    common = newCommon;
    if (common.length === 0) {
      return "None";
    }
  }
  return common.length > 0 ? common[0][0] : "None";
}
console.log(
  getMeetingTime([
    [
      [7, 8],
      [10, 12],
      [13, 15],
    ],
    [
      [8, 11],
      [12, 13],
      [14, 15],
    ],
    [
      [6, 7],
      [8, 9],
      [12, 13],
    ],
  ]),
);
