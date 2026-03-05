let poll = new Map([
  ["Dark Souls 1", new Set(["Gywn", "Solair"])],
  ["Dark Souls 2", new Set(["Vendric", "Nashandra"])],
  ["Dark Souls 3", new Set(["Firekeeper"])],
]);

function addOption(option) {
  if (option.trim() === "") {
    return "Option cannot be empty.";
  } else if (!poll.has(option)) {
    poll.set(option, new Set());
    return `Option "${option}" added to the poll.`;
  } else {
    return `Option "${option}" already exists.`;
  }
}

function vote(option, voterId) {
  if (!poll.has(option)) {
    return `Option "${option}" does not exist.`;
  } else {
    if (poll.get(option).has(voterId)) {
      return `Voter ${voterId} has already voted for "${option}".`;
    } else {
      poll.get(option).add(voterId);
      return `Voter ${voterId} voted for "${option}".`;
    }
  }
}

function displayResults() {
  let result = "Poll Results:\n";
  poll.forEach((value, key) => {
    result += `${key}: ${value.size} votes\n`;
  });
  result = result.slice(0, -1);
  return result;
}

console.log(displayResults(poll));
