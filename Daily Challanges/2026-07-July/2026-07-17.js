function daysUntilBirthday(today, birthday) {
  const [year, month, day] = today.split("-").map(Number);
  const [birthMonth, birthDay] = birthday.split("/").map(Number);
  const todayDate = new Date(year, month - 1, day);

  function nextBirthday(startYear) {
    let y = startYear;

    while (true) {
      const d = new Date(y, birthMonth - 1, birthDay);
      if (
        d.getFullYear() === y &&
        d.getMonth() === birthMonth - 1 &&
        d.getDate() === birthDay
      ) {
        return d;
      }
      y++;
    }
  }

  let birthdayDate = nextBirthday(year);

  if (birthdayDate <= todayDate) {
    birthdayDate = nextBirthday(birthdayDate.getFullYear() + 1);
  }

  return Math.round((birthdayDate - todayDate) / 86400000);
}

console.log(daysUntilBirthday("2026-07-16", "9/7"));
console.log(daysUntilBirthday("2026-07-16", "3/22"));
console.log(daysUntilBirthday("2026-07-16", "7/16"));
console.log(daysUntilBirthday("2024-02-28", "3/1"));
console.log(daysUntilBirthday("2023-04-24", "12/30"));
console.log(daysUntilBirthday("2024-03-01", "2/29"));
console.log(daysUntilBirthday("2096-03-01", "2/29"));
