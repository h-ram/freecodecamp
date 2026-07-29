function getLoanSchedule(amount, annualRate, monthlyPayment) {
  let balance = amount;
  const schedule = [Math.round(balance)];
  const monthlyRate = annualRate / 100 / 12;

  while (balance > 0) {
    balance += balance * monthlyRate;
    balance -= monthlyPayment;

    if (balance < 0) {
      balance = 0;
    }

    schedule.push(Math.round(balance));
  }

  return schedule;
}

console.log(getLoanSchedule(1000, 0, 200));
console.log(getLoanSchedule(1000, 5, 200));
console.log(getLoanSchedule(10, 50, 1));
console.log(getLoanSchedule(5500, 8, 400));
console.log(getLoanSchedule(50000, 5.2, 1650));
