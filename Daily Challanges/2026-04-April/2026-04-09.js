function getNextBingoNumber(n) {
  let bNum = (Number(n.slice(1)) % 75) + 1;
  if (bNum < 16) return `B${bNum}`;
  else if (bNum < 31) return `I${bNum}`;
  else if (bNum < 46) return `N${bNum}`;
  else if (bNum < 61) return `G${bNum}`;
  else return `O${bNum}`;
}

console.log(getNextBingoNumber("B10"));
