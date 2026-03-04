const currentDate = new Date();
const currentDateFormat = `Current Date and Time: ${currentDate}`;

console.log(currentDateFormat);
console.log();

function formatDateMMDDYYYY(date) {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();
  return `Formatted Date (MM/DD/YYYY): ${month}/${day}/${year}`;
}

function formatDateLong(date) {
  const month = date.toLocaleString("default", { month: "long" });
  const day = date.getDate();
  const year = date.getFullYear();
  return `Formatted Date (Month Day, Year): ${month} ${day}, ${year}`;
}

console.log(formatDateMMDDYYYY(currentDate), "\n");
console.log(formatDateLong(currentDate), "\n");
