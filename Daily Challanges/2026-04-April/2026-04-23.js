function getDirection(time1, time2) {
  const [h1, m1] = time1.split(":").map((item) => Number(item));
  const [h2, m2] = time2.split(":").map((item) => Number(item));
  let t1 = h1 * 60 + m1;
  let t2 = h2 * 60 + m2;

  const forward = (t2 - t1 + 1440) % 1440;
  const backward = 1440 - forward;

  if (forward < backward) return "forward";
  else if (backward < forward) return "backward";
  else return "equal";
}

console.log(getDirection("10:00", "12:00"));
console.log(getDirection("11:00", "05:00"));
console.log(getDirection("00:00", "12:00"));
console.log(getDirection("15:45", "01:10"));
console.log(getDirection("03:30", "19:50"));
console.log(getDirection("06:30", "18:30"));
