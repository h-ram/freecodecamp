function britishToAmerican(sentence) {
  const words = {
    colour: "color",
    flavour: "flavor",
    honour: "honor",
    neighbour: "neighbor",
    labour: "labor",
    humour: "humor",
    centre: "center",
    fibre: "fiber",
    defence: "defense",
    offence: "offense",
    organise: "organize",
    recognise: "recognize",
    analyse: "analyze",
  };

  for (const [brit, amer] of Object.entries(words)) {
    sentence = sentence.replace(new RegExp(brit, "gi"), (m) =>
      [...m].every((c) => c >= "A" && c <= "Z")
        ? amer.toUpperCase()
        : m[0] === m[0].toUpperCase()
          ? amer[0].toUpperCase() + amer.slice(1)
          : amer,
    );
  }

  return sentence;
}

console.log(britishToAmerican("I love the colour blue."));
console.log(britishToAmerican("The fibre optic cable is new."));
console.log(
  britishToAmerican("It's an honour to meet someone with such humour."),
);
console.log(
  britishToAmerican(
    "The unrecognised artist analysed his colour palette at the centre.",
  ),
);
console.log(
  britishToAmerican(
    "The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful.",
  ),
);
