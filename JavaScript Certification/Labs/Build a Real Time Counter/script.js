const textInput = document.querySelector("#text-input");
const charCount = document.querySelector("#char-count");

textInput.addEventListener("input", handleInput);

function handleInput(event) {
  const limit = 50;
  const val = event.target.value;
  const len = val.length;
  if (len > limit) {
    event.target.value = val.slice(0, limit);
  } else {
    charCount.textContent = `Character Count: ${len}/50`;
  }
  if (len >= limit) {
    charCount.classList.add("limit-exceeded");
  } else {
    charCount.classList.remove("limit-exceeded");
  }
}
