function getElementSize(windowSize, elementVw, elementVh) {
  const [width, height] = windowSize.split("x").map((item) => Number(item));
  const vw = parseInt(elementVw);
  const vh = parseInt(elementVh);

  const newWidth = (width * vw) / 100;
  const newHeight = (height * vh) / 100;
  return `${newWidth} x ${newHeight}`;
}

const test1 = getElementSize("1200 x 800", "50vw", "50vh");
const test2 = getElementSize("320 x 480", "25vw", "50vh");
const test3 = getElementSize("1000 x 500", "7vw", "3vh");
const test4 = getElementSize("1920 x 1080", "95vw", "100vh");
const test5 = getElementSize("1200 x 800", "0vw", "0vh");
const test6 = getElementSize("1440 x 900", "100vw", "114vh");

const check1 = "600 x 400";
const check2 = "80 x 240";
const check3 = "70 x 15";
const check4 = "1824 x 1080";
const check5 = "0 x 0";
const check6 = "1440 x 1026";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
