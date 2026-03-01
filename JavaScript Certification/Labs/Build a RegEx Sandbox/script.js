const regexPattern = document.getElementById("pattern");
const stringToTest = document.getElementById("test-string");
const testButton = document.getElementById("test-btn");
const testResult = document.getElementById("result");

const caseInsensitiveFlag = document.getElementById("i");
const globalFlag = document.getElementById("g");

function getFlags() {
  let flags = "";
  if (caseInsensitiveFlag.checked) flags += "i";
  if (globalFlag.checked) flags += "g";
  return flags;
}

testButton.addEventListener("click", () => {
  const flags = getFlags();
  const regex = new RegExp(regexPattern.value, flags);

  const inputText = stringToTest.innerHTML;
  const matches = inputText.match(regex);

  if (!matches) {
    testResult.textContent = "no match";
    return;
  }

  testResult.textContent = matches.join(", ");

  const highlighted = inputText.replace(regex, match =>
    `<span class="highlight">${match}</span>`
  );

  stringToTest.innerHTML = highlighted;
});