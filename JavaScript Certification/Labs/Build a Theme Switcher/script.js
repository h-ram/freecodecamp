const themeSwitcherBtn = document.querySelector("#theme-switcher-button");
const themeDropdown = document.querySelector("#theme-dropdown");
const themeBtns = document.querySelectorAll('[role="menuitem"]');
const liveText = document.querySelector("[aria-live]");

const themes = [
  { name: "light", message: "Flashbang!" },
  { name: "dark", message: "Booo!" },
];

themeSwitcherBtn.addEventListener("click", () => {
  const isOpen = !themeDropdown.hidden;

  themeDropdown.hidden = isOpen;
  themeSwitcherBtn.setAttribute("aria-expanded", String(!isOpen));
});

themeBtns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const selectedId = e.target.id;
    const selectedThemeName = selectedId.replace("theme-", "");

    document.body.className = selectedId;

    const themeObj = themes.find((theme) => theme.name === selectedThemeName);

    if (themeObj) {
      liveText.textContent = themeObj.message;
    }

    themeDropdown.hidden = true;
    themeSwitcherBtn.setAttribute("aria-expanded", "false");
  });
});
