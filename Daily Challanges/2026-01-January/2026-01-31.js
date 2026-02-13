function getSign(dateStr) {
    const [, month, day] = dateStr.split('-').map(Number);
    
    if ((month === 3 && day >= 21) || (month === 4 && day <= 19))
        return "Aries";
    else if ((month === 4 && day >= 20) || (month === 5 && day <= 20))
        return "Taurus";
    else if ((month === 5 && day >= 21) || (month === 6 && day <= 20))
        return "Gemini";
    else if ((month === 6 && day >= 21) || (month === 7 && day <= 22))
        return "Cancer";
    else if ((month === 7 && day >= 23) || (month === 8 && day <= 22))
        return "Leo";
    else if ((month === 8 && day >= 23) || (month === 9 && day <= 22))
        return "Virgo";
    else if ((month === 9 && day >= 23) || (month === 10 && day <= 22))
        return "Libra";
    else if ((month === 10 && day >= 23) || (month === 11 && day <= 21))
        return "Scorpio";
    else if ((month === 11 && day >= 22) || (month === 12 && day <= 21))
        return "Sagittarius";
    else if ((month === 12 && day >= 22) || (month === 1 && day <= 19))
        return "Capricorn";
    else if ((month === 1 && day >= 20) || (month === 2 && day <= 18))
        return "Aquarius";
    else 
        return "Pisces";
}

const test1 = getSign("2026-01-31");
const test2 = getSign("2001-06-10");
const test3 = getSign("1985-09-07");
const test4 = getSign("2023-03-19");
const test5 = getSign("2045-11-05");
const test6 = getSign("1985-12-06");
const test7 = getSign("2025-12-30");
const test8 = getSign("2018-10-08");
const test9 = getSign("1958-05-04");

const check1 = "Aquarius";
const check2 = "Gemini";
const check3 = "Virgo";
const check4 = "Pisces";
const check5 = "Scorpio";
const check6 = "Sagittarius";
const check7 = "Capricorn";
const check8 = "Libra";
const check9 = "Taurus";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);
console.log(`Test8: ${test8 === check8}`);
console.log(`Test9: ${test9 === check9}`);