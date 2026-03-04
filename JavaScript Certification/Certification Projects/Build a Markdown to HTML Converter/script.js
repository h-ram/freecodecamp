const mdInput = document.querySelector("#markdown-input");
const htmlOutput = document.querySelector("#html-output");
const preview = document.querySelector("#preview");
mdInput.addEventListener("input", convertMarkdown);

const regexH1 = /^\s*#{1} (.+)/gm;
const regexH2 = /^\s*#{2} (.+)/gm;
const regexH3 = /^\s*#{3} (.+)/gm;
const regexBold1 = /\*\*(.+)\*\*/gm;
const regexBold2 = /__(.+)__/gm;
const regexItalic1 = /\*(.+)\*/gm;
const regexItalic2 = /_(.+)_/gm;
const regexImg = /!\[(.+)\]\((.+)\)/gm;
const regexAnchor = /\[(.+)\]\((.+)\)/gm;
const regexQuote = /^>\s+(.+)/gm;

function convertMarkdown() {
  const text = mdInput.value;
  const html = text
    .replace(regexH3, "<h3>$1</h3>")
    .replace(regexH2, "<h2>$1</h2>")
    .replace(regexH1, "<h1>$1</h1>")
    .replace(regexBold1, "<strong>$1</strong>")
    .replace(regexBold2, "<strong>$1</strong>")
    .replace(regexItalic1, "<em>$1</em>")
    .replace(regexItalic2, "<em>$1</em>")
    .replace(regexImg, '<img src="$2" alt="$1">')
    .replace(regexAnchor, '<a href="$2">$1</a>')
    .replace(regexQuote, "<blockquote>$1</blockquote>");
  htmlOutput.textContent = html;
  preview.innerHTML = html;

  return html;
}
