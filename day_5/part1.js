const fs = require("fs");
const FILEPATH = "./input.txt";
const filecontent = fs.readFileSync(FILEPATH, "utf-8").split("\n");

const check = (num, ranges) => {
  for (let [x, y] of ranges) {
    if (num < x) return false;
    if (num >= x && num <= y) return true;
  }
  return false;
};

const solve = (inp) => {
  let [ranges, ids] = [
    inp.slice(0, inp.indexOf("")),
    inp.slice(inp.indexOf("") + 1),
  ];
  ranges = ranges
    .map((x) => x.split("-").map((x) => +x))
    .sort((x, y) => x[0] - y[0]);
  ids = ids.map((x) => +x);

  return ids.reduce((acum, cur) => (check(cur, ranges) ? 1 + acum : acum), 0);
};

console.log(solve(filecontent));
