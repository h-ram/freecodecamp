function medicationReminder(medications, currentTime) {
  function toMin(t) {
    const [h, m] = t.split(":").map(Number);
    return h * 60 + m;
  }

  const now = toMin(currentTime);
  let bestName = "";
  let bestWait = Infinity;

  for (const [name, last] of medications) {
    const lastMin = toMin(last);
    let nextT;

    if (name === "Mergeflictamine") {
      nextT = lastMin + 240;
      while (nextT <= now) {
        nextT += 240;
      }
    } else if (name === "Deployxitrin") {
      const schedule = [480, 960];
      nextT = schedule.find((t) => t > now);
      if (nextT === undefined) nextT = schedule[0] + 1440;
    } else {
      const schedule = [420, 780, 1260];
      nextT = schedule.find((t) => t > now);
      if (nextT === undefined) nextT = schedule[0] + 1440;
    }

    const wait = nextT - now;

    if (wait < bestWait) {
      bestWait = wait;
      bestName = name;
    }
  }

  const h = Math.floor(bestWait / 60);
  const m = bestWait % 60;

  return `${bestName} in ${h}h ${m}m`;
}

console.log(
  medicationReminder(
    [
      ["Deployxitrin", "08:00"],
      ["Debuggamanizole", "07:00"],
      ["Mergeflictamine", "10:00"],
    ],
    "11:00",
  ),
);
