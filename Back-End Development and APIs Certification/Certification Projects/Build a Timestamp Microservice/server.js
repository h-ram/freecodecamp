import express from "express";
import cors from "cors";

const app = express();

app.use(cors({ optionsSuccessStatus: 200 }));

app.use(express.static("public"));

app.get("/", (_req, res) => {
  res.sendFile(import.meta.dirname + "/views/index.html");
});

// Do not change code above this line

app.get("/api", (req, res)=>{
  const now = new Date();
  res.json({
    unix: now.getTime(),
    utc: now.toUTCString(),
  });
})

app.get("/api/:date", (req, res) => {
  const dateParam  = req.params.date;
  let date;

  // If dateParam consists only of digits, treat it as a Unix timestamp (integer)
  if (/^\d+$/.test(dateParam)) {
    date = new Date(parseInt(dateParam, 10));
  } else {
    // Parse standard date strings (e.g "2015-12-25")
    date = new Date(dateParam);
  }

  // If the date object is invalid, return the error JSON
  if (isNaN(date.getTime())) {
    return res.json({ error: "Invalid Date" });
  }

  // Return the parsed Unix timestamp (number) and UTC string
  return res.json({
    unix: date.getTime(),
    utc: date.toUTCString(),
  });
});

// Do not change code below this line

const PORT = 8000;
const listener = app.listen(PORT, function () {
  console.log("Your app is listening on port " + listener.address().port);
});
