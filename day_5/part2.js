const fs = require("fs");
const FILEPATH = "./input.txt";
const filecontent = fs.readFileSync(FILEPATH, "utf-8").split("\n");

const solve = (inp) => {
  let ranges = inp.slice(0, inp.indexOf(""));
  ranges = ranges
    .map((x) => x.split("-").map((x) => +x))
    .sort((x, y) => x[0] - y[0]);
  let res = [];
  let i = 1;
  let [tmpSmall, tmpLarge] = [ranges[0][0], ranges[0][1]];
  while (i < ranges.length) {
    let [p1, p2] = ranges[i];
    if (p1 > tmpLarge) {
      res.push([tmpSmall, tmpLarge]);
      tmpSmall = p1;
      tmpLarge = p2;
    } else {
      tmpLarge = Math.max(p2, tmpLarge);
    }
    i += 1;
  }
  res.push([tmpSmall, tmpLarge]);
  return res.reduce((acum, cur) => acum + cur[1] - cur[0] + 1, 0);
};

console.log(solve(filecontent));
