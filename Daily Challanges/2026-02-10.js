function totalSecs(time) {
    const [h, m, s] = time.split(':');
    return parseInt(h) * 3600 + parseInt(m) * 60 + parseInt(s);
}

function getRelativeResults(results) {
    const winnerSecs = totalSecs(results[0]);
    const times = ["0"];
    
    for (let i = 1; i < results.length; i++) {
        const playerSecs = totalSecs(results[i]);
        const diff = playerSecs - winnerSecs;
        const minutes = Math.floor(diff / 60);
        const secs = diff % 60;
        times.push(`+${minutes}:${secs.toString().padStart(2, '0')}`);
    }
    
    return times;
}

const test1 = getRelativeResults(["1:25:32", "1:26:10", "1:27:05"]);
const test2 = getRelativeResults(["1:00:01", "1:00:05", "1:00:10"]);
const test3 = getRelativeResults(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]);
const test4 = getRelativeResults(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]);
const test5 = getRelativeResults(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]);

const check1 = ["0", "+0:38", "+1:33"];
const check2 = ["0", "+0:04", "+0:09"];
const check3 = ["0", "+0:17", "+0:42", "+2:05"];
const check4 = ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"];
const check5 = ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);