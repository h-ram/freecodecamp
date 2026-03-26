function getMovieNightCost(day, showtime, numberOfTickets) {
  let ticketCost = ["Friday", "Saturday", "Sunday"].includes(day) ? 12.0 : 10.0;
  let hour = Number(showtime.split(":")[0]);
  const meridiem = showtime.slice(-2);
  if (meridiem === "pm") {
    hour += 12;
  }
  if (hour < 17 && day !== "Tuesday") {
    ticketCost -= 2.0;
  }

  if (day === "Tuesday") {
    ticketCost = 5.0;
  }
  const totalCost = ticketCost * numberOfTickets;
  return `$${totalCost.toFixed(2)}`;
}

console.log(getMovieNightCost("Saturday", "10:00pm", 1));
