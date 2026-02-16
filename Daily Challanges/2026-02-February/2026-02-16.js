function getSemifinalMatchups(teams) {
  let scores = []
  for(const team of teams){
    const [name, record] = team.split(":")
    let points = record.split("-");

        let total =
            parseInt(points[0]) * 3 +
            parseInt(points[1]) * 2 +
            parseInt(points[2]);

        scores.push([name, total]);
    }

    scores.sort((a, b) => b[1] - a[1]);

    const result =  `The semi-final games will be ${scores[0][0]} vs ${scores[3][0]} and ${scores[1][0]} vs ${scores[2][0]}.`;
    return result;
}


const test1 = getSemifinalMatchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]);
const test2 = getSemifinalMatchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]);
const test3 = getSemifinalMatchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]);
const test4 = getSemifinalMatchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]);

const check1 = "The semi-final games will be FIN vs SWE and CAN vs USA.";
const check2 = "The semi-final games will be USA vs CZE and CAN vs FIN.";
const check3 = "The semi-final games will be CAN vs ITA and USA vs CZE.";
const check4 = "The semi-final games will be JPN vs ITA and AUT vs KOR.";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);