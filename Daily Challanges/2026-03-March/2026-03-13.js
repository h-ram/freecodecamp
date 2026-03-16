function calculateParkingFee(parkTime, pickupTime) {
  let cost = 0;
  const [h1, m1] = parkTime.split(":").map((item) => Number(item));
  const [h2, m2] = pickupTime.split(":").map((item) => Number(item));
  let parkMinutes = h1 * 60 + m1;
  let pickMinutes = h2 * 60 + m2;
  if (pickMinutes <= parkMinutes) {
    cost += 10;
    pickMinutes += 24 * 60;
  }
  const diff = pickMinutes - parkMinutes;
  cost += Math.ceil(diff / 60) * 3;
  cost = Math.max(cost, 5);
  return `$${cost}`;
}

const test1 = calculateParkingFee("09:00", "11:00");
const test2 = calculateParkingFee("10:00", "10:30");
const test3 = calculateParkingFee("08:10", "10:45");
const test4 = calculateParkingFee("14:40", "23:10");
const test5 = calculateParkingFee("18:15", "01:30");
const test6 = calculateParkingFee("11:11", "11:10");

const check1 = "$6";
const check2 = "$5";
const check3 = "$9";
const check4 = "$27";
const check5 = "$34";
const check6 = "$82";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
