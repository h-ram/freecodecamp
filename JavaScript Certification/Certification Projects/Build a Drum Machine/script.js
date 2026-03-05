const display = document.querySelector("#display");
const pads = document.querySelectorAll(".drum-pad");

function playSound(key) {
  const audio = document.getElementById(key);
  if (!audio) return;
  audio.currentTime = 0;
  audio.play();
  display.textContent = audio.parentElement.id;
}

pads.forEach((pad) => {
  pad.addEventListener("click", () => {
    const key = pad.textContent.trim().toUpperCase();
    playSound(key);
  });
});

document.addEventListener("keydown", (e) => {
  playSound(e.key.toUpperCase());
});
