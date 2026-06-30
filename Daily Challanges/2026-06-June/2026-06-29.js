function getMood(genre, bpm) {
  if (bpm >= 60 && bpm <= 109 && genre === "classical") {
    return "focus";
  } else if (bpm >= 60 && bpm <= 89 && genre === "electronic") {
    return "focus";
  } else if (bpm >= 60 && bpm <= 180 && genre === "pop") {
    return "happy";
  } else if (bpm >= 110 && bpm <= 180 && genre === "classical") {
    return "happy";
  } else if (bpm >= 60 && bpm <= 129 && genre === "rock") {
    return "happy";
  } else if (bpm >= 90 && bpm <= 134 && genre === "electronic") {
    return "happy";
  } else if (bpm >= 130 && bpm <= 180 && genre === "rock") {
    return "hype";
  } else if (bpm >= 135 && bpm <= 180 && genre === "electronic") {
    return "hype";
  }

  return "Unknown";
}

console.log(getMood("rock", 111));
console.log(getMood("electronic", 74));
console.log(getMood("classical", 180));
console.log(getMood("rock", 155));
console.log(getMood("electronic", 90));
console.log(getMood("classical", 67));
console.log(getMood("pop", 100));
console.log(getMood("electronic", 135));
