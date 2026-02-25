const footballTeam = {
  team: "Winterfell Wolves",
  year: 2026,
  headCoach: "Jon Snow",
  players: [
    { name: "Arya Stark", position: "forward", isCaptain: false },
    { name: "Brienne of Tarth", position: "defender", isCaptain: true },
    { name: "Tyrion Lannister", position: "midfielder", isCaptain: false },
    { name: "Samwell Tarly", position: "goalkeeper", isCaptain: false },
    { name: "Daenerys Targaryen", position: "forward", isCaptain: false },
  ],
};

document.getElementById("team").textContent = footballTeam.team;
document.getElementById("year").textContent = footballTeam.year;
document.getElementById("head-coach").textContent = footballTeam.headCoach;

const playerCards = document.querySelector("#player-cards");
const positionFilter = document.querySelector("#players");

positionFilter.addEventListener("change", handleFilter);

function buildCards(filter = "all") {
  let playersString = "";
  footballTeam.players.forEach((player) => {
    if (player.position != filter && filter != "all") {
      return;
    }
    const temp = `<div class="player-card">
      <h2>${player.isCaptain ? "(Captain) " : ""}${player.name}</h2>
      <p>Position: ${player.position}</p>
    </div>`;
    playersString += temp;
  });

  playerCards.innerHTML = playersString;
}

buildCards();

function handleFilter({ target }) {
  console.log(target.value);
  buildCards(target.value);
}
