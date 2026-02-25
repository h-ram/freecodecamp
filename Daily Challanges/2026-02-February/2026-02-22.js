function countMedals(winners) {
  let csv = "Country,Gold,Silver,Bronze,Total\n";
  const countries = {};

  for (const event of winners) {
    const [g, s, b] = event;

    if (!countries[g]) countries[g] = [0, 0, 0];
    if (!countries[s]) countries[s] = [0, 0, 0];
    if (!countries[b]) countries[b] = [0, 0, 0];

    countries[g][0] += 1;
    countries[s][1] += 1;
    countries[b][2] += 1;
  }

  // Convert to sortable array
  const sorted = Object.entries(countries).sort(
    ([countryA, medalsA], [countryB, medalsB]) => {
      // Sort by gold descending
      if (medalsA[0] !== medalsB[0]) {
        return medalsB[0] - medalsA[0];
      }
      // Then alphabetical
      return countryA.localeCompare(countryB);
    },
  );

  for (const [country, medals] of sorted) {
    const [g, s, b] = medals;
    const total = g + s + b;
    csv += `${country},${g},${s},${b},${total}\n`;
  }

  return csv.trim();
}

const test1 = countMedals([
  ["USA", "CAN", "NOR"],
  ["NOR", "USA", "CAN"],
  ["USA", "NOR", "SWE"],
]);
const test2 = countMedals([["NOR", "SWE", "FIN"]]);
const test3 = countMedals([
  ["ITA", "CHN", "CHN"],
  ["JPN", "ITA", "JPN"],
]);
const test4 = countMedals([
  ["USA", "CAN", "NOR"],
  ["GER", "FRA", "ITA"],
  ["JPN", "KOR", "CHN"],
  ["SWE", "FIN", "NOR"],
  ["CAN", "USA", "SWE"],
  ["FRA", "GER", "ITA"],
]);
const test5 = countMedals([
  ["ESP", "ITA", "FRA"],
  ["ITA", "ESP", "GER"],
  ["NOR", "SWE", "FIN"],
  ["FIN", "NOR", "SWE"],
  ["USA", "CAN", "MEX"],
  ["CAN", "USA", "MEX"],
  ["JPN", "KOR", "CHN"],
  ["CHN", "JPN", "KOR"],
]);
const test6 = countMedals([
  ["USA", "CAN", "GER"],
  ["NOR", "SWE", "FIN"],
  ["USA", "NOR", "SWE"],
  ["GER", "FRA", "ITA"],
  ["JPN", "KOR", "CHN"],
  ["USA", "GER", "CAN"],
  ["SWE", "NOR", "FIN"],
  ["CAN", "USA", "NOR"],
  ["FRA", "GER", "ITA"],
  ["JPN", "CHN", "KOR"],
  ["SWE", "FIN", "NOR"],
  ["GER", "ITA", "FRA"],
]);

const check1 =
  "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1";
const check2 =
  "Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1";
const check3 =
  "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2";
const check4 =
  "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2";
const check5 =
  "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2";
const check6 =
  "Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
