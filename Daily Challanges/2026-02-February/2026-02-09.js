function skiJumpMedal(distancePoints, stylePoints, windComp, kPointBonus) {
    const place1 = 180.0
    const place2 = 175.0
    const place3 = 172.0

    const score = distancePoints + stylePoints + windComp + kPointBonus

    if(score > place1){
      return "Gold"
    }else if(score > place2){
      return "Silver"
    }else if(score > place3){
      return "Bronze"
    }else{
      return "No Medal"
    }
}

const test1 = skiJumpMedal(125.0, 58.0, 0.0, 6.0);
const test2 = skiJumpMedal(119.0, 50.0, 1.0, 4.0);
const test3 = skiJumpMedal(122.0, 52.0, -1.0, 4.0);
const test4 = skiJumpMedal(118.0, 50.5, -1.5, 4.0);
const test5 = skiJumpMedal(124.0, 50.5, 2.0, 5.0);

const check1 = "Gold";
const check2 = "Bronze";
const check3 = "Silver";
const check4 = "No Medal";
const check5 = "Gold";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);