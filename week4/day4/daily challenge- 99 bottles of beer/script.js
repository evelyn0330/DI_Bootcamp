let startBottles = prompt(
  "Give me a number to start counting beers down from!"
);
let count = 1;

console.log(
  startBottles +
    " bottles of beer on the wall\n" +
    startBottles +
    " bottles of beer\n" +
    "Take " +
    count +
    " down, pass it around"
);
startBottles = +startBottles - count;
count++;

do {
  console.log(
    startBottles +
      " bottles of beer on the wall\n" +
      startBottles +
      " bottles of beer\n" +
      "Take " +
      count +
      " down, pass them around"
  );
  startBottles = +startBottles - count;
  count++;
} while (startBottles > 0);
console.log("No more bottles of beer.");
