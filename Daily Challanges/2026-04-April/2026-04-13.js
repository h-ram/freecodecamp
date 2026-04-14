function getInitials(name) {
  const parts = name.split(" ");
  let initials = "";
  for (let part of parts) {
    initials += part[0].toUpperCase() + ".";
  }
  return initials;
}

console.log(getInitials("Tommy Millwood"));
console.log(getInitials("Savanna Puddlesplash"));
console.log(getInitials("Frances Cowell Conrad"));
