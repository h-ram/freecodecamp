// Lesson 01
const fs = require("fs")
console.log(fs)

// Lesson 02
console.log(fs.readFileSync("./assets/poem.txt"))

// Lesson 03
const syncData = fs.readFileSync("./assets/poem.txt", { encoding: "utf8" })
console.log(syncData)

// Lesson 04
const asyncData = fs.readFile("./assets/poem.txt", {encoding: "utf8"}, (err,data) =>{
    console.log(data)
})

// Lesson 05
const fsPromises = require("fs/promises");
async function main() {
  const data = await fsPromises.readFile("./assets/poem.txt", {
    encoding: "utf8",
  });
  console.log(data);
}
main();

// Lesson 06
fs.writeFileSync("./assets/output.txt", "Hello, freeCodeCamp!")

// Lesson 07
fs.appendFileSync("./assets/output.txt", "\nSecond line")

// Lesson 08
console.log(fs.existsSync("./assets/output.txt"))

// Lesson 09
const folder = fs.readdirSync("./assets")
console.log(folder)

// Lesson 10
const buf = Buffer.from("Hello, Node!");
console.log(buf);

// Lesson 11
console.log(buf.toString("hex"))
console.log(buf.toString("base64"))

// Lesson 12
const buf2 = Buffer.alloc(8,0xff)
console.log(buf2)

// Lesson 13
const decoded = Buffer.from("ZnJlZUNvZGVDYW1w", "base64").toString("utf8");
console.log(decoded)

// Lesson 14
const crypto = require("crypto")
const hash = crypto.createHash("sha256").update("freeCodeCamp!").digest("hex")
console.log(hash)

// Lesson 15
const random = crypto.randomBytes(16).toString("hex");
console.log(random);

// Lesson 16
const id = crypto.randomUUID();
console.log(id);

// Lesson 17
const os = require("os");
console.log(os.platform())
console.log(os.arch())
console.log(os.hostname())

// Lesson 18
console.log(os.totalmem())
console.log(os.freemem())
console.log(os.uptime())

// Lesson 19
console.log(os.cpus().length)

// Lesson 20
const path = require("path");
const fullPath = path.join(__dirname, "assets", "poem.txt");
console.log(fullPath);

// Lesson 21
console.log(path.basename(fullPath))
console.log(path.dirname(fullPath))
console.log(path.extname(fullPath))

// Lesson 22
console.log(path.join('assets', '..', 'server.js'))
console.log(path.resolve('assets', '..', 'server.js'))

// Lesson 23
console.log(path.parse(fullPath))

// Lesson 24
console.log(process.version)
console.log(process.platform)
console.log(process.env.NODE_ENV)

// Lesson 25
console.log(process.argv)

// Lesson 26
process.stdout.write("Hello from stdout\n")
process.stderr.write("Hello from stderr\n")

// Lesson 27
const readable1 = fs.createReadStream("assets/poem.txt", { encoding: "utf8" });

readable1.on("data", (chunk) => {
  console.log(chunk);
});

readable1.on("end", () => {
  console.log("Done reading");
});

// Lesson 28
const writable1 = fs.createWriteStream("assets/stream-output.txt");
writable1.write("First chunk\n");
writable1.write("Second chunk\n");
writable1.end();

// // Lesson 29
const readable = fs.createReadStream("assets/poem.txt");
const writable = fs.createWriteStream("assets/stream-output.txt");
readable.pipe(writable);